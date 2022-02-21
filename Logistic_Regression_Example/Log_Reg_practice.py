import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

%tensorflow_version 2.x
from tensorflow.keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train/255.0 # Normalizing between 0 and 1
X_test = X_test/255.0 # Normalizing between 0 and 1


print("X_train shape", X_train.shape)
print("y_train shape", y_train.shape)
print("X_test shape", X_test.shape)
print("y_test shape", y_test.shape)

fig, axs = plt.subplots(nrows=4, ncols=4, figsize=(10, 6), subplot_kw={'xticks': [], 'yticks': []})
i = 0
for ax in axs.flat:
  ax.imshow(X_train[i,:,:], cmap='Greys')
  i += 1


X_train = X_train.reshape(X_train.shape[0],X_train.shape[1]*X_train.shape[2])
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1]*X_test.shape[2])

print("New X_train shape", X_train.shape)
print("New X_test shape", X_test.shape)

y_tr = y_train[(y_train==0) | (y_train==1)]
y_ts = y_test[(y_test==0) | (y_test==1)]
X_tr = X_train[(y_train==0) | (y_train==1),:]
X_ts = X_test[(y_test==0) | (y_test==1),:]

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential()
model.add(layers.Dense(1, activation='sigmoid',input_dim=X_tr.shape[1]))
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
model.summary()

history = model.fit(X_tr, y_tr, epochs = 10, verbose = 1, validation_data=(X_ts, y_ts))

from tensorflow.keras.utils import to_categorical
num_class = 10
Y_train = to_categorical(y_train, num_class)
Y_test = to_categorical(y_test, num_class)

print(Y_train)

model2 = keras.Sequential()
model2.add(layers.Dense(num_class, activation='softmax',input_dim=X_tr.shape[1]))
model2.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
model2.summary()

history2 = model2.fit(X_train, Y_train, epochs = 10, verbose = 1, validation_data=(X_test, Y_test))


# plot learning curves
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15, 6))
#ax1.set_title('Learning Curves')
ax1.set_xlabel('Epoch', fontsize=18)
ax1.set_ylabel('Cross Entropy', fontsize=18)
ax1.grid(which='both')
ax1.minorticks_on()
ax1.plot(history2.history['loss'], label='train_loss')
ax1.plot(history2.history['val_loss'], label='val_loss')
ax1.tick_params(labelsize=15)
ax1.legend(loc='best',fontsize=15)

ax2.set_xlabel('Epoch', fontsize=18)
ax2.set_ylabel('Accuracy', fontsize=18)
ax2.grid(which='both')
ax2.minorticks_on()
ax2.plot(history2.history['accuracy'], label='train_accuracy')
ax2.plot(history2.history['val_accuracy'], label='val_accuracy')
ax2.tick_params(labelsize=15)
ax2.legend(loc='best',fontsize=15)
fig.suptitle('Original Network', fontsize=20)


Y_Pred = np.argmax(model2.predict(X_test), axis=-1)
df = pd.DataFrame([y_test,Y_Pred]).T
df.columns = ['Test','Predicted']
confusion_matrix = pd.crosstab(df['Test'], df['Predicted'], rownames=['Test'], colnames=['Predicted'])

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(confusion_matrix, annot=True, fmt='d', ax=ax, cmap="YlGnBu")
plt.show()


missed = np.where(y_test != Y_Pred)[0] # indices of miss classified imaged

missed_imgs = X_test[missed,:].reshape(-1,28,28) # missed images from test dataset
missed_true = y_test[missed] # true labels of missed images
missed_pred = Y_Pred[missed] # predicted labels of missed images


fig, axs = plt.subplots(nrows=4, ncols=4, figsize=(10, 8), subplot_kw={'xticks': [], 'yticks': []})
i = 0
for ax in axs.flat:
  ax.imshow(missed_imgs[i,:,:], cmap='Greys')
  ax.set_title('Predicted:%d, True:%d'%(missed_pred[i],missed_true[i]))
  i += 1


test_image = plt.imread('any image link') # read image 
test_image = test_image/255.0 # Normalise
test_image_label = np.argmax(model2.predict(test_image.ravel().reshape(1,-1)),axis=-1) # Predict the label
print('Predicted Label is %d'%(test_image_label[0]))