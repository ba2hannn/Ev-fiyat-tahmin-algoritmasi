import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from sklearn.preprocessing import StandardScaler  # StandardScaler ekleniyor
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

# Veri setini yükleme
dataFrame = pd.read_csv("evler.csv")

# Veri setindeki eksik değerleri kontrol etme
# print(dataFrame.isnull().sum())

# Gereksiz sütunları veri setinden çıkarma
# dataFrame = dataFrame.drop("id", axis=1)
# dataFrame = dataFrame.drop("date", axis=1)
# print(dataFrame)

# Fiyat ile diğer özellikler arasındaki korelasyonu kontrol etme
# print(dataFrame.corr()["price"].sort_values())

# Fiyat dağılımını görselleştirme
# sbn.displot(dataFrame["price"])

# En yüksek fiyatlı %1'lik verileri çıkarma ve fiyat dağılımını tekrar görselleştirme
# yuzdeDoksanDokuzDf = dataFrame.sort_values("price", ascending=False).iloc[220:]
# sbn.displot(yuzdeDoksanDokuzDf["price"])
# dataFrame = yuzdeDoksanDokuzDf

# Bağımlı değişken ve bağımsız değişkenlerin tanımlanması
y = dataFrame["price"].values
x = dataFrame.drop("price", axis=1).values

# Veri standardizasyonu
scaler = StandardScaler()  # MinMaxScaler yerine StandardScaler kullanılıyor
x = scaler.fit_transform(x)

# Eğitim ve test veri setlerini ayırma
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=10)

# Model oluşturma
model = Sequential()

model.add(Dense(64, activation="relu"))
model.add(Dropout(0.2))  # Dropout oranını ayarlayın (örneğin, %20)
model.add(Dense(32, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")

# Erken Durma (Early Stopping) için geri çağırma
early_stopping = EarlyStopping(patience=10, restore_best_weights=True)

# Öğrenme Oranı Azaltma (Learning Rate Decay) için geri çağırma
reduce_lr = ReduceLROnPlateau(factor=0.1, patience=5)

# Modelin eğitimi
history = model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test),
                    batch_size=32, epochs=1000, callbacks=[early_stopping, reduce_lr])

# Kayıp değerlerinin görselleştirilmesi
kayipVerisi = pd.DataFrame(model.history.history)
kayipVerisi.plot()

# Modeli kaydetme
model.save("ev_fiyati.h5")

plt.show()
