import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Input, Flatten, Dense, Dropout

def build_deep_nn(rows, columns, channels, layer_options):
     model = Sequential()
    
     # Flatten input
     model.add(Flatten(input_shape=(rows, columns, channels)))
    
     # Add hidden layers based on layer_options
     for hidden_size, activation, dropout_rate in layer_options:
        model.add(Dense(hidden_size, activation=activation))
        if dropout_rate > 0:
            model.add(Dropout(dropout_rate))
    
     # Output layer for classification (e.g., MNIST has 10 classes)
     model.add(Dense(10, activation='softmax'))
    
     # Compile the model
     model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
     return models