import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Veri setini yükleme
dataFrame = pd.read_csv("evler.csv")

# İstenmeyen sütunları veri setinden çıkarma
dataFrame = dataFrame.drop(["id", "date"], axis=1)

# # Veri setini görselleştirme
# yuzdeDoksanDokuzDf = dataFrame.sort_values("price", ascending=False).iloc[220:]
# dataFrame = yuzdeDoksanDokuzDf

# Giriş ve çıkış verilerini ayırma
y = dataFrame["price"].values
x = dataFrame.drop("price", axis=1).values

# Veri ölçeklendirme
scaler = MinMaxScaler()
x = scaler.fit_transform(x)

# Test veri setini oluşturma
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)

# Modeli yükleme
model = load_model("ev_fiyati_v4.h5")

# Gerçek değerlerin ve tahmin edilen değerlerin karşılaştırılması
tahmin = model.predict(x_test)

# Gerçek değerlerin ve tahmin edilen değerlerin farkını hesaplama
diff = y_test - tahmin.flatten()

# Sapma oranını hesaplama
deviation = round(float(diff.mean()), 2)

# Sapma oranını yüzde olarak hesaplama
deviation_percentage = round((diff.mean() / y_test.mean()) * 100, 2)

# Scatter plot
df = pd.DataFrame({'Gerçek Değerler': y_test, 'Tahmin Edilen Değerler': tahmin.flatten()})

# Boyutları ve renkleri güncelleme
plt.figure(figsize=(10, 6))
sns.set_palette("husl")  # Renk paletini güncelleme

# Scatter plot
sns.regplot(data=df, x='Gerçek Değerler', y='Tahmin Edilen Değerler', scatter_kws={'alpha': 0.7}, line_kws={'color': 'lime', 'linewidth': 2})

# Doğru ekleme
sns.lineplot(x=[min(y_test), max(y_test)], y=[min(y_test), max(y_test)], color='red', label='Ideal Doğru')

# Eksen etiketlerini güncelleme
plt.xlabel('Gerçek Değerler', fontsize=12)
plt.ylabel('Tahmin Edilen Değerler', fontsize=12)

# Başlık ve ek bilgiler ekleme
plt.title('Gerçek ve Tahmin Edilen Değerlerin Karşılaştırması', fontsize=14)
plt.text(0.95, 0.05, f"Sapma Oranı: {deviation} ($)", ha='right', va='center', transform=plt.gca().transAxes, fontsize=12)
plt.text(0.95, 0.1, f"Sapma Oranı (%): {deviation_percentage}%", ha='right', va='center', transform=plt.gca().transAxes, fontsize=12)

# İlgili eksenleri genişletme
plt.xlim(min(y_test), max(y_test))
plt.ylim(min(y_test), max(y_test))

# Grid eklenmesi
plt.grid(True, linestyle='--', alpha=0.5)

# Legendayı ekleme
plt.legend(fontsize=10)

# Grafiği gösterme
plt.show()