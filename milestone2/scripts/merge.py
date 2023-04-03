import pandas as pd
filepathparquet = "./combined_model_data_parti.parquet"
df = pd.read_parquet(filepathparquet)
syd_lat = -33.86
syd_lon = 151.21

df = df[(df['lat_min'] < syd_lat) & (df['lat_max'] > syd_lat)]
df = df[(df['lon_min'] < syd_lon) & (df['lon_max'] > syd_lon)]
df = df.drop(['lat_min', 'lat_max', 'lon_min', 'lon_max'], axis=1)

df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.date
df = df.pivot_table(index='time', columns='model', values='rain (mm/day)')

df.to_csv('./ml_data_SYD.csv')

