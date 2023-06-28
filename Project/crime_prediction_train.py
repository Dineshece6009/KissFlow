import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data generators for training and testing data
train_datagen = ImageDataGenerator(...)
test_datagen = ImageDataGenerator(...)

# Load training and testing data
train_data = train_datagen.flow_from_directory(train_folder_path, ...)
test_data = test_datagen.flow_from_directory(test_folder_path, ...)

# Model architecture and training
model = create_model()
model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, validation_data=test_data, epochs=EPOCHS)
