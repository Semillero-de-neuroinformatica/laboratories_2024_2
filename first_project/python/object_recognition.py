import os
import shutil

import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import regularizers
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping

IMG_HEIGHT = 224
IMG_WIDTH = 224

PATH_TO_DATA = 'database'  
TRAIN_DIR = 'database/train'
VAL_DIR= 'database/val'
TEST_DIR= 'database/test'

def create_dataset():
    categories = ['palm', 'fist']

    for category in categories:
        img_dir = os.path.join(PATH_TO_DATA, category)
        imgs = os.listdir(img_dir)
	    
        train_imgs, test_imgs = train_test_split(imgs, test_size=0.2, random_state=42)
        val_imgs, test_imgs = train_test_split(test_imgs, test_size=0.5, random_state=42)
    
        for img in train_imgs:
            shutil.move(os.path.join(img_dir, img), os.path.join(TRAIN_DIR, category, img)) 

        for img in val_imgs:
            shutil.move(os.path.join(img_dir, img), os.path.join(VAL_DIR, category, img))
	        
        for img in test_imgs:
            shutil.move(os.path.join(img_dir, img), os.path.join(TEST_DIR, category, img))


def fetch_data():

    train_datagen = ImageDataGenerator(
	    rescale=1./255, 
	    rotation_range=40,
	    width_shift_range=0.2,
	    height_shift_range=0.2,
	    shear_range=0.2,
	    zoom_range=0.2,
	    horizontal_flip=True,
	    fill_mode='nearest',
        brightness_range=[0.8, 1.2],
        channel_shift_range=0.2,
        vertical_flip=True,
        validation_split=0.2,
	)

    val_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
	    TRAIN_DIR,
	    target_size=(224, 224),
	    batch_size=8,
	    class_mode='binary'
	)
	
    val_generator = val_datagen.flow_from_directory(
	    VAL_DIR,
	    target_size=(224, 224),
	    batch_size=8,
	    class_mode='binary'
	)

    test_generator = test_datagen.flow_from_directory(
            TEST_DIR,
            target_size=(224, 224),
            batch_size=8,
            class_mode='binary'
    )

    return train_generator, val_generator, test_generator 

def build_model():

    model = models.Sequential([
        layers.Input(shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01)),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(16, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01)),
        layers.Conv2D(16, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01)),
        layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01)),
       
        layers.Flatten(),
        layers.Dropout(0.6),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.summary()

    return model

def visualize_training_results(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(len(acc))

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

    

def main() -> None:
    
    #create_dataset()
    train_generator, val_generator, test_generator = fetch_data()
    model = build_model()

    lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1)


    history = model.fit(
        train_generator,
        epochs=20,
        validation_data=val_generator,
        callbacks=[lr_scheduler, early_stopping]
    )

    visualize_training_results(history)

    test_loss, test_acc = model.evaluate(test_generator)
    print(f"Precisión en el conjunto de testeo: {test_acc * 100:.2f}%")

    model.evaluate(val_generator)

    model.save('model.h5')


if __name__ == '__main__':
    main()
