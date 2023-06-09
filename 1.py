
import pandas as pd


df = pd.read_csv('source_data.csv')
df['date'] = pd.to_datetime(df['date'])
df_january = df.loc[df['date'].dt.month == 1]
df_day = df_january[df_january['date'].dt.day == 1]
print(df_day)
print(df.head())
print(df.dtypes)

#1
non_zero_orders = len(df_day[df_day['order_price'] != 0])
print("Количество заказов за 1 января, где order_price не равно 0: ", non_zero_orders)

#2
total_orders = len(df_day)
print("Общее количество заказов за 1 января: ", total_orders)
zero_orders = len(df_day[df_day['order_price'] == 0])
print("Количество заказов за 1 января, где order_price равно 0: ", zero_orders)
percent_zero_orders = zero_orders / total_orders * 100
print("Процент заказов за 1 января, где order_price равно 0: ", round(percent_zero_orders, 2), "%")

#3
zero_price_days = df.loc[df['order_price'] == 0, 'date'].dt.date.unique()
print("Дни, в которые были заказы с order_price равным 0: ", zero_price_days)

#4
orders_by_user = df.groupby('uid')['order_id'].count()
top100_users = orders_by_user.nlargest(100)
print(top100_users)

#5
cutlery_orders = df[df['cutlery'] > 0]
user_orders = cutlery_orders.groupby('uid')['cutlery'].count()
top10_users = user_orders.sort_values(ascending=False).head(10)
print(top10_users)

#6
tip_orders = df[df['tips'] > 0]
user_tips = tip_orders.groupby('uid')['tips'].sum()
top_users = user_tips.sort_values(ascending=False).head(20)
print(top_users)

#7
tip_days = df.groupby('date')['tips'].sum()
top_days = tip_days.sort_values(ascending=False).head(20)
print(top_days)

#8
popular_cutlery = df[df['cutlery'] > 0]
num_popular_cutlery = popular_cutlery['cutlery'].unique()
print("Количество популярных столовых приборов:", num_popular_cutlery)

#9
num_unique_users = df['uid'].nunique()
print("Количество уникальных пользователей:", num_unique_users)

#10
df['time_of_day'] = df['date'].dt.hour.apply(lambda x: 'night' if x < 6 else 'morning' if x < 12 else 'afternoon' if x < 18 else 'evening')
orders_by_time_of_day = df.groupby('time_of_day')['order_id'].count()
print(orders_by_time_of_day)

#11
grouped_data = df.groupby('uid')['order_price'].sum()
top10_users = grouped_data.sort_values(ascending=False)[:10]
print(top10_users)

#12
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.date
df_grouped = df.groupby('day')['order_id'].count()
df_sorted = df_grouped.sort_values(ascending=False)
top5_days = df_sorted.head(5)
print(top5_days)


