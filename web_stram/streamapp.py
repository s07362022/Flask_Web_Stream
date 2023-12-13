from flask import Flask, render_template, Response
import cv2
from yolo_cap_detect import yolo_detect

app = Flask(__name__)
camera = cv2.VideoCapture(0)

img_path = './img'

def gen_frames():
    count = 0
    while True:
        success, frame = camera.read()
        frame = yolo_detect(frame,path_name=img_path,count=count)
        count+=1
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0')