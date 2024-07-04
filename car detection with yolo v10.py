import os
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import random

# YOLO modelini yükle
model = YOLO("yolov10x.pt")

# Görüntüde nesne tahmini yapma işlevi
def predict_and_detect(model, img_path, conf=0.5):
    img = cv2.imread(img_path)  # Görüntüyü oku
    results = model.predict(img, conf=conf)  # YOLO modeli ile tahmin yap
    for result in results:
        for box in result.boxes:
            # Her nesne için kutu çiz ve etiketi ekle
            cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                          (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), 2)
            cv2.putText(img, f"{result.names[int(box.cls[0])]}",
                        (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
    return img

# Test görüntülerini al
img_dir = "../input/car-object-detection/data/testing_images"
onlyfiles = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]
random_files = random.sample(onlyfiles, 10)  # Rastgele 10 dosya seç

# Görüntüleri işle ve göster
plt.figure(figsize=(32, 80))
for i, filename in enumerate(random_files, 1):
    img_path = os.path.join(img_dir, filename)
    result_img = predict_and_detect(model, img_path)
    plt.subplot(10, 2, i)
    plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
