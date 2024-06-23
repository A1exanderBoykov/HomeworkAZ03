import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы, которую будем парсить
url = "https://www.divan.ru/category/divany"

# Отправка HTTP-запроса на страницу
response = requests.get(url)
response.raise_for_status()  # проверка на успешность запроса

# Парсинг HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение данных о диванах
divans = soup.find_all('div', class_='product-card')
data = []
for divan in divans:
    name = divan.find('a', class_='product-card__name').text.strip()
    price = divan.find('span', class_='product-card__price').text.strip()
    price = int(price.replace(' ', '').replace('₽', ''))  # Преобразование цены в числовой формат
    data.append([name, price])

# Создание DataFrame из полученных данных
df = pd.DataFrame(data, columns=['Name', 'Price'])

# Сохранение данных в CSV-файл
df.to_csv('divans_prices.csv', index=False)

# Вычисление средней цены
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Построение гистограммы цен
plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.show()