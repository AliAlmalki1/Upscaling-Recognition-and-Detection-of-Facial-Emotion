# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QffEOxk2gKGmRWTvF8m40Dl2zOcqqwrE
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.layers import Flatten, Dense
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator , img_to_array, load_img
from keras.applications.mobilenet import MobileNet, preprocess_input
from keras.losses import categorical_crossentropy

base_model = MobileNet( input_shape=(224,224,3), include_top= False )

for layer in base_model.layers:
  layer.trainable = False


x = Flatten()(base_model.output)
x = Dense(units=7 , activation='softmax' )(x)

model = Model(base_model.input, x)

model.compile(optimizer='adam', loss= categorical_crossentropy , metrics=['accuracy']  )

train_datagen = ImageDataGenerator(zoom_range = 0.2,shear_range = 0.2,horizontal_flip=True,rescale = 1./255)

train_data = train_datagen.flow_from_directory(directory= "/content/train",target_size=(224,224),batch_size=32,)

train_data.class_indices

{'angry': 0,'disgust': 1, 'fear': 2, 'happy': 3, 'neutral': 4, 'sad': 5, 'surprise': 6}

val_datagen = ImageDataGenerator(rescale = 1./255 )

val_data = val_datagen.flow_from_directory(directory= "/content/test",target_size=(224,224),batch_size=32,)


t_img , label = train_data.next()

def plotImages(img_arr, label):
  """
  input  :- images array
  output :- plots the images
  """
  count = 0
  for im, l in zip(img_arr,label) :
    plt.imshow(im)
    plt.title(im.shape)
    plt.axis = False
    plt.show()

    count += 1
    if count == 20:
      break

plotImages(t_img, label)


from keras.callbacks import ModelCheckpoint, EarlyStopping

es = EarlyStopping(monitor='val_accuracy', min_delta= 0.01 , patience= 5, verbose= 1, mode='auto')

mc = ModelCheckpoint(filepath="best_model.h5", monitor= 'val_accuracy', verbose= 1, save_best_only= True, mode = 'auto')

call_back = [es, mc]

hist = model.fit_generator(train_data,
                           steps_per_epoch= 10,
                           epochs= 30,
                           validation_data= val_data,
                           validation_steps= 8,
                           callbacks=[es,mc])

from keras.models import load_model
model = load_model("/content/best_model.h5")

h =  hist.history
h.keys()

op = dict(zip( train_data.class_indices.values(), train_data.class_indices.keys()))

path = "/content/test/angry/PrivateTest_10131363.jpg"

img = load_img(path, target_size=(224,224) )

i = img_to_array(img)/255
input_arr = np.array([i])
input_arr.shape

pred = np.argmax(model.predict(input_arr))

print(f" the person in the image is {op[pred]}")

plt.imshow(input_arr[0])
plt.title(f" the person in the image is {op[pred]}")
plt.show()

import cv2

def upscale_image(image_path, scale_factor=2):
    img = cv2.imread(image_path)

    upscaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    return upscaled_img

image_path = path
upscaled_image = upscale_image(image_path, scale_factor=2)

cv2.imwrite(path, upscaled_image)

plt.imshow(upscaled_image)
plt.title("upscal")
plt.show()


img = load_img(path, target_size=(224,224) )

i = img_to_array(img)/255
input_arr = np.array([i])
input_arr.shape

pred = np.argmax(model.predict(input_arr))

print(f" the person in the image is {op[pred]}")

plt.imshow(input_arr[0])
plt.title(f" the person in the image is {op[pred]}")
plt.show()

img = load_img(path, target_size=(224, 224))

i = img_to_array(img) / 255
input_arr = np.array([i])
input_arr.shape

pred = np.argmax(model.predict(input_arr))

print(f" the person in the image is {op[pred]}")

plt.subplot(1,3,1)
plt.imshow(input_arr[0])
plt.title(f" the person in the image is {op[pred]}")

import cv2


def upscale_image(image_path, scale_factor=2):
    img = cv2.imread(image_path)

    upscaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    return upscaled_img


image_path = path
upscaled_image = upscale_image(image_path, scale_factor=2)

cv2.imwrite(path, upscaled_image)

plt.subplot(1,3,2)
plt.imshow(upscaled_image)
plt.title("upscal")

img = load_img(path, target_size=(224, 224))

i = img_to_array(img) / 255
input_arr = np.array([i])
input_arr.shape

pred = np.argmax(model.predict(input_arr))

print(f" the person in the image is {op[pred]}")

plt.subplot(1,3,3)

plt.imshow(input_arr[0])
plt.title(f" the person in the image is {op[pred]}")
plt.show()
