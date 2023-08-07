import pandas as pd 
import cv2
import numpy as np
import argparse
ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help="Image Path")
args=vars(ap.parse_args())
img_path=args['image']
img=cv2.imread(img_path)
clicked=False
r=g=b=xpos=ypos=0
index=["color","color_name","hex","R","G","B"]
colors=pd.read_csv('colors.csv',names=index,header=None)
def getColorName(R,G,B):
    min=10000
    for i in range(len(colors)):
        d=abs(R-int(colors.loc[i,"R"]))+abs(G-int(colors.loc[i,"G"]))+abs(B-int(colors.loc[i,"B"]))
        if(d<min):
            min=d
            cname=colors.loc[i,"color_name"]
    return cname
def draw_function(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global r,g,b,xpos,ypos,clicked
        clicked=True
        xpos=x
        ypos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
            
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)
while(1):
    cv2.imshow("image",img)
    if(clicked):
        cv2.rectangle(img,(20,20),(900,69),(b,g,r),-1)
        text=getColorName(r,g,b)+'R='+str(r)+"G="+str(g)+"B="+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()
        