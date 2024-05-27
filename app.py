import os

from flask import Flask, request, jsonify
from logic.db_conection.requests import get_urls_emails, set_status_result, add_record
from logic.emails.result_sendler import send_email
from logic.google_drive.download import download_photo
from templates.test_on_dataset import predict_car
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

'''def upload_file():
    data = get_urls_emails()
    urls = [row[0] for row in data]
    emails = [row[1] for row in data]
    id = [row[2] for row in data]
    for url, email, id in zip(urls, emails, id):
        download_photo(url)
        result = predict_car(os.path.join('templates', 'uploads', 'photo.jpg'))
        send_email(email, url, result)
        os.remove('templates/uploads/photo.jpg')
        set_status_result(id, 'done', result)

    return True'''

'''@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        data = get_urls_emails()
        urls = [row[0] for row in data]
        emails = [row[1] for row in data]
        id = [row[2] for row in data]
        for url, email, id in zip(urls, emails, id):
            download_photo(url)
            result = predict_car(os.path.join('templates', 'uploads', 'photo.jpg'))
            send_email(email, url, result)
            os.remove('templates/uploads/photo.jpg')
            set_status_result(id, 'done', result)

        return True'''


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    email = data['email']
    add_record(url, email)

    download_photo(url)
    result = predict_car(os.path.join('templates', 'uploads', 'photo.jpg'))
    send_email(email, url, result)
    os.remove('templates/uploads/photo.jpg')
    set_status_result(url, email, 'done', result)

    return jsonify({'message': 'Record added successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
