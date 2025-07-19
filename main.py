# !pip install ultralytics

from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("best.pt")
# source ="0" means using my webcam
results = model.predict(source="0", show=True)