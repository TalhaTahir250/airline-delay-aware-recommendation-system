import trino
import pandas as pd

# === CONFIG — fill in your values ===
OPENSKY_USER = "talha721"         # OpenSky web username (lowercase)
OPENSKY_PASS = "@WroGj73"         # OpenSky web password
# ------------------------------------

conn = trino.dbapi.connect(
    host="trino.opensky-network.org",
    port=443,
    user=OPENSKY_USER,
    catalog="minio",
    schema="osky",
    http_scheme="https",
    auth=trino.auth.BasicAuthentication(OPENSKY_USER, OPENSKY_PASS)
)

cursor = conn.cursor()

# Example: fetch flight-level history (small range)
query = """
SELECT *
FROM flights_data4
LIMIT 500
"""

cursor.execute(query)

# Fetch into pandas
rows = cursor.fetchall()
cols = [col[0] for col in cursor.description]
df = pd.DataFrame(rows, columns=cols)

print(df.head())
print("Rows fetched:", len(df))
