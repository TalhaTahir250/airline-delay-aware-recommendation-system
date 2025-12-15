Airline Delay–Aware Flight Recommendation System
Overview

This project aims to provide a real-world flight recommendation system by predicting expected flight delays and recommending optimal flights to passengers. The system leverages live and historical flight data from the OpenSky Network API and combines it with machine learning models to estimate arrival delays.

The goal is to help users choose flights that are least likely to be delayed based on real-time tracking, historical performance, weather conditions, and operational trends.

Features

Live Flight Data Collection: Continuous retrieval of aircraft state vectors (position, velocity, altitude, callsign, etc.) from the OpenSky API.

Historical Flight Data Analysis: Processing and merging of historical flight arrivals for predictive insights.

Data Cleaning & Preprocessing: Handling missing values, duplicates, and outliers to prepare data for modeling.

Delay Prediction: Machine learning models to predict flight arrival delays.

Flight Recommendation: Rank flights based on predicted delay, reliability, and operational metrics.

Export & Visualization: Cleaned datasets stored for analysis, with tools to visualize aircraft trajectories and trends.

Data Sources

OpenSky Network API: Provides live aircraft state vectors and flight arrivals.

Historical Flight Data: Collected through OpenSky’s Trino SQL interface (requires approved access).

Derived Features: Velocity, altitude trends, time-of-day patterns, airport congestion metrics.
