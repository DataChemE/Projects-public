import tensorflow as tf 
from keras import layers
from keras.models import Sequential
from keras.optimizers import Adam
import keras.utils
from keras.callbacks import LearningRateScheduler


image_size = 224
batch_size = 64

training_set = '/Users/tylerjensen/Desktop/portfolio projects/Alzheimer_s Dataset/train'
testing_set = '/Users/tylerjensen/Desktop/portfolio projects/Alzheimer_s Dataset/test'

class_labels = [
    'MildDemented',
    'ModerateDemented',
    'NonDemented',
    'VeryMildDemented']

testing_dataset = keras.utils.image_dataset_from_directory(testing_set, image_size=(image_size, image_size), 
    batch_size=batch_size, 
    seed=42, 
    labels='inferred', 
    label_mode='categorical', 
    class_names=class_labels)


training_generator = keras.utils.image_dataset_from_directory(training_set, 
    validation_split=.2, 
    subset='training', 
    image_size=(image_size, image_size), 
    batch_size=batch_size, 
    seed=42, 
    labels='inferred', 
    label_mode='categorical', 
    class_names=class_labels)



testing_generator = keras.utils.image_dataset_from_directory(training_set, 
    validation_split=.2, 
    subset='validation', 
    image_size=(image_size, image_size), 
    batch_size=batch_size, 
    seed=42, 
    labels = 'inferred', 
    label_mode='categorical', 
    class_names=class_labels)


model = Sequential()
model.add(layers.Flatten(input_shape=(image_size, image_size,3)))
model.add(layers.Dense(4, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(4))
model.add(layers.Activation('softmax'))

metrics = [tf.keras.metrics.AUC(name='auc'), tf.keras.metrics.CategoricalAccuracy(name = 'categorical_accuracy')]

opt = Adam(learning_rate=.0001)

model.compile(optimizer = opt, loss = 'categorical_crossentropy', metrics = metrics )

model.fit(training_generator, validation_data = testing_generator, epochs=10)

model.evaluate(testing_dataset)
