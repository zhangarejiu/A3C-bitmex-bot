

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding
from keras.layers import LSTM, Bidirectional
from keras import backend as K


class God_brain:
    def __init__(self,NUM_STS):
        self.max_features = 4
        self.batch_size = 128
        self.embedding_dims = 50
        self.lstm_dims = 100
        self.nb_epoch = 10
        self.output_dims = 3

    def _build_model(self):
        model = Sequential()
        model.add(Embedding(self.max_features, self.embedding_dims, input_length=self.maxlen))
        model.add(LSTM(self.lstm_dims))
        model.add(Dense(self.output_dims, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
