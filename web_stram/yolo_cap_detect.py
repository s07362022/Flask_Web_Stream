import cv2
import numpy as np
# import pandas as pd
import datetime
import pprint
#from pymongo import MongoClient
# import pandas as pd
# import json
# import imutils
# import time
# from datetime import datetime
# import RPi.GPIO as GPIO
# import time


#YOLO_network
# net = cv2.dnn.readNetFromDarknet("yolov4-tiny.cfg","yolov4-tiny_last.weights")

# layer_names = net.getLayerNames()
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# classes = [line.strip() for line in open("obj.names")]
# colors = [(0,0,255),(255,0,0),(0,255,0)]

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
# img = yolo_detect(frame,path_name=img_path,count=count)

#def record(img_name,label,x,y,w,h,result):
  
 # df=pd.DataFrame() 
 # result = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
  #grades = [["test","Sensor/yolo",img_name,label,x,y,w,h,result]]
  #data = pd.DataFrame(grades)
  #df=df.append(data,ignore_index=True)
 # df.columns = ['measurement','topic','img_name','label','x','y','w','h','time'] 
  #print(df)  

  
  

# VIDEO_IN = cv2.VideoCapture(0)

# while True:
#     hasFrame, frame = VIDEO_IN.read()
#     if hasFrame!=False:
#         img = yolo_detect(frame,path_name=img_path,count=count)
#         cv2.imshow("Frame", imutils.resize(img, width=640,height=480))#imutils.resize(img), width=, width=860
#         count=count+1
#     else:
#         pass
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# VIDEO_IN.release()    
# cv2.destroyAllWindows()


 

 
 

