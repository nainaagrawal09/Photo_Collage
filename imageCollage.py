import cv2
import pandas as pd
import numpy as np

img1=cv2.imread("top_left.jpg")
img2=cv2.imread("top_right.jpg")
img3=cv2.imread("bottom_left.jpg")
img4=cv2.imread("bottom_right.jpg")
img5=cv2.imread("center.jpeg")

#colouring
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img3=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
img4=cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)
img5=cv2.cvtColor(img5,cv2.COLOR_BGR2RGB)

#Resizing it
img1=cv2.resize(img1,(200,200))
img2=cv2.resize(img2,(200,200))
img3=cv2.resize(img3,(200,200))
img4=cv2.resize(img4,(200,200))
img5=cv2.resize(img5,(100,100))

#Adding Borders
oimg1=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=[0,0,0])
oimg2=cv2.copyMakeBorder(img2,10,10,0,10,cv2.BORDER_CONSTANT,value=[0,0,0])
oimg3=cv2.copyMakeBorder(img3,0,10,10,10,cv2.BORDER_CONSTANT,value=[0,0,0])
oimg4=cv2.copyMakeBorder(img4,0,10,0,10,cv2.BORDER_CONSTANT,value=[0,0,0])
oimg5=cv2.copyMakeBorder(img5,10,10,10,10,cv2.BORDER_CONSTANT,value=[0,0,0])

o1=np.concatenate((oimg1,oimg2),axis=1)
o2=np.concatenate((oimg3,oimg4),axis=1)
o=np.concatenate((o1,o2))
o[155:275,155:275]=oimg5[:,:]
#o=np.reshape(o,(430*430,3))
#df=pd.DataFrame(o,dtype='int32',columns=['r','g','b'])
#df.to_csv("cllage.csv",index=False)
cv2.imshow("output",o)
cv2.waitKey(0)
cv2.destroyAllWindows()


