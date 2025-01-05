## 🎣 FishBotAI

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)

🐟 API for detecting a float while fishing in the game World of Warcraft.

## 🛠 Usage
- Send image to endpoint `/get_coords`
- If a float is detected, the coordinates of the middle of the float are returned:
```
{
  "x": 1286.51,
  "y": 581.28
}
```
:point_right: [Model](https://drive.google.com/file/d/1NpGiD6enqiqrCVCBrlgG67kuOO4YyH6f/view?usp=sharing/)
:point_right: [Dataset](https://universe.roboflow.com/wow-float/wow-fishing-fnjeg/dataset/1)

## ⚙ What does it look like:
<img src="https://github.com/StefanEpic/fishbotAI/blob/main/work/test.jpg" width="800">

<img src="https://github.com/StefanEpic/fishbotAI/blob/main/work/result.png" width="800">
