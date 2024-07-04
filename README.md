# car-detection-using-yolo-v10
---

# Araç Algılama Uygulaması

Bu proje, YOLO (You Only Look Once) nesne algılama modeli kullanılarak görüntülerdeki araçları ve trafik ışıklarını algılamak ve görselleştirmek için yapılmış bir örnektir.

## Kurulum

1. **Gereksinimler**
   - Python 3.x
   - OpenCV (`pip install opencv-python`)
   - Matplotlib (`pip install matplotlib`)
   - Ultralytics YOLO (`pip install ultralytics`)

2. **YOLO Modelinin Yüklenmesi**
   - YOLOv10 model dosyasını (`yolov10x.pt`) indirin veya eğitilmiş bir model dosyasını kullanın.

3. **Projenin İndirilmesi**
   - Proje dosyalarını bu repodan indirin veya klonlayın:

     ```bash
     git clone https://github.com/kullaniciadi/projeadi.git
     cd projeadi
     ```

## Kullanım

1. **Görüntüleri Hazırlama**
   - Test edilecek görüntüleri `data/testing_images` dizinine yerleştirin.

2. **Kodun Çalıştırılması**
   - Görüntüleri işlemek ve araçları algılamak için `detect_objects.py` dosyasını çalıştırın:

     ```bash
     python detect_objects.py
     ```

   - `detect_objects.py` dosyası, seçilen rastgele 10 görüntü üzerinde araç algılama yapacak ve sonuçları görsel olarak gösterecektir.

## Katkıda Bulunma

- Eğer bir hata bulursanız veya bir öneriniz varsa, lütfen bir Issue açın veya bir Pull Request gönderin.

---
