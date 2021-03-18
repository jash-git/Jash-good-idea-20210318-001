import cv2
import numpy as np

flag = False
x1=y1=0

def gen_light(rect):
  global temp2,result,dst,temp
  temp2 = temp.copy() #原图备份
  mask1 = np.zeros(temp2.shape, temp2.dtype)
  cv2.rectangle(mask1,rect,(255,255,255),-1)
  result = cv2.seamlessClone(temp2, dst, mask1, (400,200), cv2.MONOCHROME_TRANSFER)
  cv2.imshow('result',result)
def screenShot(event,x,y,flags,param):
  global x1,y1,flag,img,temp
  if event==cv2.EVENT_LBUTTONDOWN: #鼠标左键按下
    flag = True #表示当前鼠标左键是按下的
    x1 = x
    y1 = y
  elif event==cv2.EVENT_MOUSEMOVE: #鼠标移动
    if(flag):
      img = temp.copy()#原图复制(把绘制的矩形清空)
      cv2.rectangle(img,(x1,y1),(x,y),(0,255,0),2)
  elif event==cv2.EVENT_LBUTTONUP: #鼠标左键弹起
    flag = False
    ROI = temp[y1:y,x1:x] #---y1:y2, x1:x2
    gen_light((x1,y1,x-x1,y-y1))
    
img = cv2.imread('light.jpg') #读取图像
dst = cv2.imread("./2.jpg")
temp = img.copy() #原图备份

cv2.imshow("result", dst)

cv2.namedWindow('selectROI')

cv2.setMouseCallback('selectROI',screenShot)

while(1):
  cv2.imshow('selectROI',img)
  if cv2.waitKey(1)&0xFF==27: #Esc按下退出
    break

cv2.destroyAllWindows()