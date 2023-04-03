import pandas as pd
import s3fs

# Load raw data
s3_path = 's3://mds2023-group6/combined_model_data_parti.parquet'
fs = s3fs.S3FileSystem()

with fs.open(s3_path, 'rb') as f:
    df = pd.read_parquet(f)

# Filter to keep Sydney data only
syd_lat = -33.86
syd_lon = 151.21

df = df[(df['lat_min'] < syd_lat) & (df['lat_max'] > syd_lat)]
df = df[(df['lon_min'] < syd_lon) & (df['lon_max'] > syd_lon)]

# Drop redundant columns
df = df.drop(['lat_min', 'lat_max', 'lon_min', 'lon_max'], axis=1)

# Re-format time
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.date

# Pivot dataframe
df = df.pivot_table(index='time', columns='model', values='rain (mm/day)')

# Save to csv
s3_path = 's3://mds2023-group6/output/ml_data_SYD.csv'
fs = s3fs.S3FileSystem()

with fs.open(s3_path, 'w') as f:
    df.to_csv(f)
