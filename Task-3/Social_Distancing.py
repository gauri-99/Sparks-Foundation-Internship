# TASK 3 - Social Distancing Detection
# Name - Gauri Dumbre

import numpy as np 
import cv2

#Load Yolo
net = cv2.dnn.readNet("F:/Open-CV/Object Detection/yolov3.weights","F:/Open-CV/Object Detection/yolov3.cfg")
classes=[]
with open ("F:/Open-CV/Object Detection/Names_list","r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

#Getting image
img = cv2.imread("F:/Open-CV/Object Detection/people3.png")
img = cv2.resize(img,(580,395))
height,width,channels = img.shape

#Detecting objects
blob = cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)

net.setInput(blob)
outs = net.forward(output_layers)

#showing info on the screen
class_ids = []
confidences =[]
boxes =[]
centers = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            #Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w/2)
            y = int(center_y - h/2)

            centers.append([center_x,center_y])
            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
            
index = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
no_objects = len(boxes)
font = cv2.FONT_HERSHEY_PLAIN
count = 0

for i in range(no_objects):
    if i in index:
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        for j in range(no_objects):
            if (j in index) and (i!=j):
                m,n = centers[i]
                m1,n1 = centers[j]
                r = int(((m-m1)**2 + (n-n1)**2)**0.5)   #Calculating distance between two persons
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)                
                if r<70:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    count = count+1    
                    break
              
cv2.putText(img,'Social Distancing Violations = ',(width-300,20),font,1,(0,0,0),2)
cv2.putText(img,str(count),(width-40,20),font,1,(0,0,0),2)       
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()