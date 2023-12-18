import cv2
import numpy as np
import time
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

TELEGRAM_BOT_TOKEN = "6338972908:AAF4S04_V5iB9zmTLdwyd94xyWehx9xFyDk"
TELEGRAM_CHAT_ID = "reemplazar esto por tu chat id"  # <-- chat id de mi cuenta

camera_name = "Calle #8 de obrajes"

bot = Bot(token=TELEGRAM_BOT_TOKEN)

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getUnconnectedOutLayersNames()

cap = cv2.VideoCapture(0)

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
            if confidence > 0.5 and class_id == 2:  # si no me equivoco esto es 'car' xd
                temp_vehicle_count += 1

    if temp_vehicle_count >= 3:
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time > 5:  # <---- cambiar el tiempo de detenccion
            message = "¡Encontramos tráfico en", camera_name, "! tome sus precauciones"
            asyncio.run(bot.send_message(chat_id=TELEGRAM_CHAT_ID,
                        text=message, parse_mode=ParseMode.MARKDOWN))
            break  # <--- error al entrar en loop, no se pueden enviar muchos mensajes

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
