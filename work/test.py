import os.path

import cv2
from ultralytics import YOLO

# Загрузите модель
curr_dir = os.path.abspath('work')
model_path = os.path.join(os.path.dirname(curr_dir), 'model.pt')
test_path = os.path.join(curr_dir, 'test.jpg')

model = YOLO(model_path)

# Выполните обнаружение объектов на изображении
results = model(test_path)

# Загрузите исходное изображение
image = cv2.imread(test_path)

# Обработка результатов
for result in results:
    boxes = result.boxes  # Получаем все обнаруженные объекты
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]  # Координаты (x1, y1) - верхний левый угол и (x2, y2) - нижний правый угол
        confidence = box.conf[0]  # Уверенность в распознавании
        class_id = int(box.cls[0])  # ID класса объекта

        # Отображение ограничивающей рамки на изображении
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.putText(image, f'Class: {class_id}, Conf: {confidence:.2f}',
                    (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Сохраните или покажите изображение с рамками
cv2.imshow("Detected Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()