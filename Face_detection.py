# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:07:18 2020

@author: KIIT
"""

import cv2
fd = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
vid = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX
while True:
  r,i = vid.read() #storing the input video captured
  gray = cv2.cvtColor (i,cv2.COLOR_BGR2GRAY) #converting to grayscale image
  f = fd.detectMultiScale(gray,1.3,7) #to detect the features of the image stored in gray
  #Multiscale returns a list with coordinates len,breadth,width,height as x,y,w,h
  for x,y,w,h in f:
    cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,0),2)
  cv2.imshow('face',i)
  k = cv2.waitKey(1)   
  if(k == ord('q')):
    break        #IF Q is pressed loop will break and video will stop

cv2.destroyAllWindows()
vid.release()