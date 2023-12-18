# Super Detector De Trafico

Este código implementa la detección de vehículos en un video utilizando el modelo YOLO (You Only Look Once). A continuación, se proporcionan los requisitos y pasos para ejecutar el código.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas y componentes:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- python-telegram-bot (`pip install python-telegram-bot`)

Se puede instalar directamente todo haciendo un:

```bash
pip install requirements.txt
```

## Descargas adicionales

Además de las bibliotecas de Python, necesitarás descargar algunos archivos externos y modelos preentrenados:

1. Descarga el archivo de pesos del modelo YOLOv3: [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights).
2. Descarga el archivo de configuración del modelo YOLOv3: [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg).
3. Descarga el archivo que contiene los nombres de las clases COCO: [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names).

Asegúrate de colocar estos archivos descargados en el mismo directorio raiz que el proyecto clonado.

## Configuración del bot de Telegram

Antes de ejecutar el script, crea un bot en Telegram y obtén el token. Para obtener el `TELEGRAM_BOT_TOKEN`, sigue los siguientes pasos:

1. Abre Telegram y busca el bot llamado "BotFather".
2. Inicia una conversación con BotFather y utiliza el comando `/newbot` para crear un nuevo bot.
3. Sigue las instrucciones y recibirás un mensaje que contiene el `TELEGRAM_BOT_TOKEN`.

## Configuración del script

Antes de ejecutar el script, asegúrate de ajustar las siguientes variables en tu código:

- `TELEGRAM_BOT_TOKEN`: Reemplaza con el token de tu bot de Telegram.
- `TELEGRAM_CHAT_ID`: Reemplaza con el ID del chat al que deseas enviar mensajes.
- `video_path`: Ruta del archivo de video que deseas analizar. Puedes cambiarlo a la ruta de tu propio video.
- Asegúrate de que los archivos descargados (`yolov3.weights`, `yolov3.cfg`, `coco.names`) estén en el mismo directorio (preferentemente que sea la misma raiz).

## Ejecución del script

Después de configurar todo, ejecuta el script. La aplicación detectará vehículos en el video y enviará un mensaje de alerta a través de Telegram si se detecta tráfico durante un período sostenido.

```bash
& C:/Python311/python.exe "<Ruta de main.py del proyecto>"
```
o tambien se podria:

```bash
python main.py
```

En caso de encontrarse en la misma raiz del proyecto

## Desarrollado por
### - Ricardo I. Valencia
### - Alejandra Garcia
