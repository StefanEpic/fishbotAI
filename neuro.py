from typing import Dict

from ultralytics import YOLO

model = YOLO("model.pt")


async def get_float_coords(image: str) -> Dict[str, float]:
    try:
        results = model(image)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                return {'x': round(float(x1 + (x2 - x1) / 2), 2), 'y': round(float(y1 + (y2 - y1) / 2), 2)}
    except:
        return {'x': 0, 'y': 0}
