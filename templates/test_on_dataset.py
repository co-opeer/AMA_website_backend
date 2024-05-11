
import os
import tensorflow as tf


from keras_tuner.src.backend import keras

model_path = os.path.join(os.path.dirname(__file__), 'saved_model_new.h5')

model = keras.models.load_model(model_path)


def predict_car(image_path):

    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array, verbose=0)
    return predictions[0] > 0.5




'''path = os.path.join( 'uploads', 'photo.jpg')
print(path)
predict_car(path)'''




