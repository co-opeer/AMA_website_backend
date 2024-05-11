import re
from google_drive_downloader import GoogleDriveDownloader as gdd



def get_id(url):
    # Шаблон для пошуку ID у URL Google Drive
    pattern = r'/file/d/([^/]+)/'

    # Пошук за допомогою регулярного виразу
    match = re.search(pattern, url)

    # Перевірка, чи було знайдено ID
    if match:
        return match.group(1)  # Повертаємо знайдений ID
    else:
        return None  # Повертаємо None, якщо ID не знайдено


def download_photo(url):
    gdd.download_file_from_google_drive(
        file_id=get_id(url),
        dest_path=r'C:\Users\PC\PycharmProjects\AMA_website_car_appearance\templates\uploads\photo.jpg')
