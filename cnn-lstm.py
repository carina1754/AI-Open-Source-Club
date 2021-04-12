from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Conv1D, MaxPooling1D
from keras.datasets import imdb
import pandas as pd
import numpy
import tensorflow as tf
import matplotlib.pyplot as plt
  
train = pd.read_csv('1.csv')
test = pd.read_csv('2.csv')

print(train.shape)
print(test.shape)

train = pd.read_csv("1.csv")
change_value_dict = {'판단유보':0,'전혀 사실 아님' : 0,'대체로 사실 아님' : 0.25,'절반의 사실' : 0.5,'대체로 사실' : 0.75, '사실' : 1}
train = train.replace({'level' : change_value_dict})

x_train = train['title']
y_train = train['level']

# 모델의 설정
model = Sequential()
model.add(Embedding(5000, 100))
model.add(Dropout(0.5))
model.add(Conv1D(64, 5, activation='relu'))
model.add(MaxPooling1D(pool_size=4))
model.add(LSTM(55))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()
  
# 모델의 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  
# 모델의 실행
history = model.fit(x_train, y_train, batch_size=100, epochs=5)
  
# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(x_test)[1]))
  
# 테스트셋의 오차
y_vloss = history.history['val_loss']
  
# 학습셋의 오차
y_loss = history.history['loss']
  
# 그래프로 표현
x_len = numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')
  
# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()