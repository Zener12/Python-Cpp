from datetime import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Графики
def Histograms(df):
    plt.title('Гистограмма открытия торгов')
    plt.hist(df['open'], bins=20, color='blue', edgecolor='black')
    plt.xlabel('Значение')
    plt.ylabel('Количество')
    plt.show()
    plt.title('Гистограмма хаев торгового дня')
    plt.hist(df['high'], bins=20, color='red', edgecolor='black')
    plt.xlabel('Значение')
    plt.ylabel('Количество')
    plt.show()
    plt.title('Гистограмма лоев торгового дня')
    plt.hist(df['low'], bins=20, color='brown', edgecolor='black')
    plt.xlabel('Значение')
    plt.ylabel('Количество')
    plt.show()
    plt.title('Гистограмма закрытия торгов')
    plt.hist(df['close'], bins=20, color='green', edgecolor='black')
    plt.xlabel('Значение')
    plt.ylabel('Количество')
    plt.show()
    plt.title('Гистограмма объемов торгов')
    plt.hist(df['baseVolume'], bins=20, color='yellow', edgecolor='black')
    plt.xlabel('Значение')
    plt.ylabel('Количество')
    plt.show()

    # Ящики с усами
def Box(df):
    plt.title('Ящик с усами открытия торгов')
    plt.boxplot(df['open'])
    plt.show()
    plt.title('Ящик с усами хаев торгов')
    plt.boxplot(df['high'])
    plt.show()
    plt.title('Ящик с усами лоев торгов')
    plt.boxplot(df['low'])
    plt.show()
    plt.title('Ящик с усами закрытия торгов')
    plt.boxplot(df['close'])
    plt.show()
    plt.title('Ящик с усами объемов торгов')
    plt.boxplot(df['baseVolume'])
    plt.show()
    plt.title('Ящик с усами общий')
    plt.boxplot(df)
    plt.show()

    # Столбчатые диаграммы
def Barh(df):
    plt.title('Столбчатые диаграммы')
    plt.barh('open', df['open'])
    plt.barh('high', df['high'])
    plt.barh('low', df['low'])
    plt.barh('close', df['close'])
    plt.barh('baseVolume', df['baseVolume'])
    plt.show()

    # Тепловая карта
def Heatmap(df):
    plt.title('Тепловая карта')
    plt.imshow(np.corrcoef(df), cmap='autumn', interpolation='nearest')
    plt.show()
def Scatter(df):
    plt.title('Точечная диаграмма')
    plt.scatter(df['open'], df['baseVolume'], s=1)
    plt.show()
def PairPlot(df):
    plt.title('Парные графики')
    sns.pairplot(df)
    plt.show()
def TimePlot(df, time):
    plt.plot(time, df['open'])
    plt.show()

df = pd.read_excel('btc_usdt.xlsx', names=['timestamp', 'open', 'high', 'low', 'close', 'baseVolume'])

timestamp_int = np.array(df['timestamp'])
timestamp_str = []
date = []

for x in timestamp_int:
    a, b = x, x
    a = dt.fromtimestamp(a).strftime("%B %d, %Y %I:%M:%S")
    timestamp_str.append(a)
    b = dt.fromtimestamp(b).strftime("%d, %I:%M:%S")
    date.append(b)


df['timestamp'] = timestamp_str
df.set_index('timestamp', inplace=True)
data_np = np.array(df)
# индексирование в датафрейме:
# 0 - дата
# 1 - цена на открытии торгов       open
# 2 - хай дня                       high
# 3 - лой дня                       low
# 4 - цена на закрытии торгов       close
# 5 - базовый объем                 baseVolume

print(df['open'].describe())
print("Медиана: ", df['open'].median())

print('\nКорреляционная матрица:')
print(np.corrcoef(df))

# print(df.groupby(['признак'].describe())