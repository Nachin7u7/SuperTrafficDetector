import cv2
import numpy as np
import time
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

TELEGRAM_BOT_TOKEN = "6338972908:AAF4S04_V5iB9zmTLdwyd94xyWehx9xFyDk"
TELEGRAM_CHAT_ID = "6416110643"  # <-- chat id de mi cuenta
camera_name = "Calle #8 de obrajes"

bot = Bot(token=TELEGRAM_BOT_TOKEN)

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getUnconnectedOutLayersNames()

# cap = cv2.VideoCapture(0) # Para usar la camara web

video_path = "coches.mp4"  # Ruta del archivo de video

cap = cv2.VideoCapture(video_path)


vehicle_count = 0
start_time = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    blob = cv2.dnn.blobFromImage(
        frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)

    temp_vehicle_count = 0

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 2:  # 'car'
                temp_vehicle_count += 1

    if temp_vehicle_count >= 3:
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time > 20:
            cv2.imwrite("last_frame.jpg", frame)

            # Enviar mensaje con la imagen
            message = f"¡Encontramos tráfico en {camera_name}! Tome sus precauciones"
            with open("last_frame.jpg", "rb") as photo:
                asyncio.run(bot.send_photo(chat_id=TELEGRAM_CHAT_ID,
                            photo=photo, caption=message, parse_mode=ParseMode.MARKDOWN))
            break  # <-- este break nos salva de desastres

    else:
        vehicle_count = 0
        start_time = None

    cv2.putText(frame, f'Coches: {temp_vehicle_count}',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('YOLO Vehicle Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
