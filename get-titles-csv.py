import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Встановлення з'єднання з Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/shkodenko.t/_bk/2023_inv/_keys/leafy-mender-238508-2eeb3680f63f.json', scope)
client = gspread.authorize(creds)

# Відкриття таблиці за ім'ям
#
# sheet_id = "1xmnp4ywN7ZVDgDC1MVF8jwQC8L5F_l8b" # Ваш ідентифікатор таблиці
# sheet = client.open_by_key(sheet_id).sheet1  # Використовуйте метод open_by_key
#
# Відкриття таблиці за ім'ям
sheet = client.open('2024-04-03 Порожній title').sheet1

# Отримання всіх записів у другому стовпчику
urls = sheet.col_values(2)

# Відкриття CSV файлу для запису
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["URL", "Title", "Datetime"])

    for url in urls:
        try:
            # Завантаження HTML сторінки
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            # Знаходження та запис тегу title
            title = soup.find('title').text
            writer.writerow([url, title, datetime.now()])
        except Exception as e:
            print(f"Error fetching {url}: {e}")

print("Data has been successfully written to output.csv")
