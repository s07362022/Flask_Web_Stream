import cv2
import numpy as np

import datetime
import pprint


CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("obj.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
net = cv2.dnn.readNet("yolov4-tiny_last.weights", "yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL_FP16)

img_path = "/home/helmat/Desktop/yolo/cap/1/"
count=1

 

def yolo_dec1(classes, scores, boxes,box_count,frame ):
    for (classid, score, box) in zip(classes, scores, boxes):
        x, y, w, h = box
        #if x - 31 < 0:
            #x = 31
        #if y - 18 < 0:
            #y = 18
        #if classid==0:
            #cut_img = frame[y - 20: y + h + 90, x - 10: x + w + 10]
        color = COLORS[int(classid) % len(COLORS)]
        box_count +=1 # 第幾位
        #print('id',box_count)
        label = "%s : %f" % (class_names[classid], score)
        cv2.rectangle(frame, box, color, 2)    #frame 
        title = 'No. %d'%(box_count)
        cv2.putText(frame, title, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
    return frame

def yolo_detect(frame,path_name,count):
    # forward propogation
    img = frame
    height, width, channels = img.shape 
    # blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), (0, 0, 0), True, crop=False)
    # net.setInput(blob)
    # outs = net.forward(output_layers)
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    box_count = 0
    frame = yolo_dec1(classes, scores, boxes,box_count,frame )
                
    return frame
img_path = './img'


 

 
 

