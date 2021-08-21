import cv2
import numpy as np
img=cv2.imread("NumberServer/025_c.png")
cv2.imshow("ropped",img)
try:
    shutil.rmtree(r"CutOut")
except:
    print("Can't Remove the Dictionary CutOut")
try:
    os.makedirs(CutOut)
except:
    print("Can't mkdir CutOut")
with open('Simplier/025_c.imgcut',encoding="utf-8") as f:
    garbage = f.readline()
    garbage = f.readline()
    garbage = f.readline()
    lines = int(f.readline())
    print(lines)
    for i in range(1,lines):
        temp1=f.readline()
        temp1 = temp1.replace('\n','')
        temp1 = temp1.split(',')
        print(temp1)
        x = int(temp1[0])
        y = int(temp1[1])
        w = int(temp1[2])
        h = int(temp1[3])
        
        crop_img = img[y:y+h,x:x+w]
        svp = "CutOut/"+str(i)+".jpg"
 #       cv2.imshow("cropped",crop_img)
        cv2.imwrite(svp,crop_img)

