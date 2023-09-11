# Ev Fiyat Tahmini Modeli

Bu proje, ev fiyatlarını tahmin etmek için kullanılan bir derin öğrenme modelini içerir. Model, ev özelliklerini kullanarak fiyat tahminleri yapabilir ve yeni verilerle eğitilebilir.

## Başlangıç

Bu talimatlar, projeyi yerel bir makinenizde çalıştırmak için gerekli adımları içerir.

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerini kurmanız gerekmektedir:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- keras

Bu kütüphaneleri pip kullanarak kurabilirsiniz:

pip install pandas numpy matplotlib seaborn scikit-learn keras

### Veri Seti

Bu model, ev özelliklerini içeren bir veri seti üzerinde eğitilmiştir. Veri setini "evler.csv" adıyla projenin ana dizinine eklemeniz gerekmektedir.

### Kullanım

Projeyi çalıştırmak için "fiyat_analizi_surum.py" dosyasını kullanabilirsiniz. Bu dosya, veri setini yükler, modeli eğitir ve sonuçları görselleştirir. Eğer modeli 1 kez kullanacaksanız ve sonrasında ihtiyacınız olmayacaksa fiyat_analizi.py dosyasını çalıştırabilirsiniz.

Analizi çalıştırmak için "analiz.py" dosyasını kullanabilirsiniz. Bu dosya, eğitilmiş modeli yükler, gerçek değerler ile tahmin edilen değerleri karşılaştırır ve sonuçları görselleştirir. Analizsonuçları, gerçek ve tahmin edilen değerlerin karşılaştırıldığı bir scatterplot (dağılım grafiği) ile görselleştirilir. Ayrıca sapma oranı ve yüzde sapma oranı da grafiğe eklenir.

## Model Yükleme

Analiz, eğitilmiş birmodelikullanır. Modeliyüklemekiçin, "ev_fiyati_vX.h5" dosyasınınyolunubelirtmelisiniz. Budosya, modelinsürümünü temsileder.

## Sonuçlar

Analiz sonuçları, gerçek ve tahmin edilen değerlerin karşılaştırılması ile görselleştirilir. Ayrıca, sapmaoranı ve yüzde sapma oranı da görüntülenir. Bu sonuçlar, modelin performansını değerlendirmek için kullanışlıdır.

## Model Geliştirme ve Sürüm Yönetimi

Bu projenin farklı sürümleri için "sürüm.txt" dosyası kullanılmaktadır. Her yeni sürümde model güncellenir ve sürüm numarası artırılır. Bu, ileride modeli geliştirmek isteyenler için izlenebilir bir sürüm yönetimi sağlar.

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak isterseniz, lütfen önerilerde bulunun veya hata düzeltmeleri yapın. Katkılarınızı göndermek için bir çekme isteği oluşturabilirsiniz.

## İletişim

Eğer herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen [e-posta adresim](mailto:makan4154@gmail.com) ile iletişime geçin.

Teşekkür ederim!
