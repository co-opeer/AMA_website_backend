
import os
import tensorflow as tf
from google_drive_downloader import GoogleDriveDownloader as gdd
from PIL import Image
from keras_tuner.src.backend import keras


model_path = os.path.join(os.path.dirname(__file__), 'saved_model.h5')

if not os.path.exists(model_path):
    gdd.download_file_from_google_drive(file_id='137uO_e5K0MpfGFwPPaOGVcpePBFe0XnA',
                                        dest_path=model_path,
                                        unzip=False)

model = keras.models.load_model(model_path)


def predict_car(image_path):
    print("try to predict car")

    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array, verbose=0)
    return predictions[0] > 0.5




'''path = os.path.join( 'uploads', 'photo.jpg')
print(path)
predict_car(path)'''




