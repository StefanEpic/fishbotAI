from ultralytics import YOLO

# Load a model
model = YOLO("yolo11l.pt")

# Train the model
train_results = model.train(
    data="./datasets/data.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=400,  # training image size
    device="0",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

# Export the model to ONNX format
path = model.export(format="onnx")  # return path to exported model
