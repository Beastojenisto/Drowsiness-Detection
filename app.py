from PIL import Image,ImageDraw,ImageFont
import numpy as np
from ultralytics import YOLO
import streamlit as st

model = YOLO('DrowsinessDetector.pt')
font_size = 40
img = st.file_uploader('Choose an Image')
font = ImageFont.truetype("arial.ttf", size=font_size)
arr = ['Awake','Drowsy']

if img is not None:
    img = Image.open(img).resize((640,640)).convert('RGB')
    results = model(img)
    for result in results:
        for i in range(len(result.boxes.cls)):
          cls = result.boxes.cls[i]
          cls = arr[int(cls)]
          lbl = result.boxes.conf[i]
          boxes = result.boxes.xyxy[i]
          draw = ImageDraw.Draw(img)
          draw.rectangle([boxes[0], boxes[1], boxes[2], boxes[3]], outline="white", width=5)
          text_position = (boxes[0]+boxes[2])/2, boxes[1]-10
          draw.text(text_position, f'{cls} {lbl}', fill="red", font=font,spacing=10)

    st.image(img,'Detected')
