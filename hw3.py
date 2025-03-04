from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
import matplotlib.pyplot as plt

# Запускаем браузер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.divan.ru/category/divany")

# Ждем, пока хотя бы один элемент с ценой появится (максимум 20 секунд)
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="price"]'))
    )
except:
    print("Цены не загрузились вовремя.")
    driver.quit()
    exit()

# Прокручиваем страницу для подгрузки товаров (можно увеличить число итераций)
for _ in range(10):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

# Собираем цены
prices_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="price"]')

prices = []
for elem in prices_elements:
    price_text = elem.text.split('руб')[0].replace('\xa0', '').replace(' ', '').strip()
    try:
        price = int(price_text)
        prices.append(price)
    except:
        continue

driver.quit()

# Проверяем, есть ли цены
if prices:
    with open('sofas_prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Цена"])
        for price in prices:
            writer.writerow([price])

    average_price = sum(prices) / len(prices)
    print(f"Средняя цена на диваны: {average_price:.2f} ₽")

    plt.hist(prices, bins=20, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.show()
else:
    print("Цены не найдены.")
