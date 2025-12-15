import os
import time
from datetime import datetime, timezone
import pandas as pd
from opensky_api import OpenSkyApi

# === CONFIGURATION ===
MASTER_FILE = "opensky_master.csv"  # master file for all data
SLEEP_INTERVAL = 5  # seconds between API requests

# === HELPER FUNCTION ===
def get_live_data(api):
    """Fetch live flight states from OpenSky."""
    states = api.get_states()
    if states is None or states.states is None:
        return None

    rows = []
    for s in states.states:
        rows.append([
            datetime.now(timezone.utc),  # snapshot time
            s.icao24,
            s.callsign.strip() if s.callsign else None,
            s.origin_country,
            s.time_position,
            s.last_contact,
            s.longitude,
            s.latitude,
            s.baro_altitude,
            s.on_ground,
            s.velocity,
            s.true_track,
            s.vertical_rate,
        ])
    return rows

# === MAIN LOOP ===
def main():
    api = OpenSkyApi()

    # Create master file with headers if it doesn't exist
    if not os.path.exists(MASTER_FILE):
        df = pd.DataFrame(columns=[
            "snapshot_time",
            "icao24",
            "callsign",
            "origin_country",
            "time_position",
            "last_contact",
            "longitude",
            "latitude",
            "baro_altitude",
            "on_ground",
            "velocity",
            "true_track",
            "vertical_rate"
        ])
        df.to_csv(MASTER_FILE, index=False)

    print(f"Appending live data to {MASTER_FILE} every {SLEEP_INTERVAL} sec...\nPress Ctrl+C to stop.")

    while True:
        try:
            rows = get_live_data(api)
            if not rows:
                print(f"{datetime.now()} - No data received. Retrying in {SLEEP_INTERVAL}s...")
                time.sleep(SLEEP_INTERVAL)
                continue

            df_new = pd.DataFrame(rows, columns=[
                "snapshot_time",
                "icao24",
                "callsign",
                "origin_country",
                "time_position",
                "last_contact",
                "longitude",
                "latitude",
                "baro_altitude",
                "on_ground",
                "velocity",
                "true_track",
                "vertical_rate"
            ])

            # Append to master CSV without index
            df_new.to_csv(MASTER_FILE, mode='a', index=False, header=False)
            print(f"{datetime.now()} - Saved {len(df_new)} rows.")

            # Wait before next request
            time.sleep(SLEEP_INTERVAL)

        except KeyboardInterrupt:
            print("\nStopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}. Retrying in {SLEEP_INTERVAL}s...")
            time.sleep(SLEEP_INTERVAL)
            continue

if __name__ == "__main__":
    main()
