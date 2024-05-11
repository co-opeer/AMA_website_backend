import os

from flask import Flask, request
from logic.db_conection.requests import get
from logic.emails.result_sendler import send_email
from logic.google_drive.download import download_photo
from templates.test_on_dataset import predict_car

app = Flask(__name__)





@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        data = get()
        urls = [row[0] for row in data]
        emails = [row[1] for row in data]
        for url, email in zip(urls, emails):
            download_photo(url)
            result = predict_car(os.path.join('templates','uploads', 'photo.jpg'))
            send_email(email, url, result)
            os.remove('templates/uploads/photo.jpg')

        return True


if __name__ == '__main__':
    app.run()




