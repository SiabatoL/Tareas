import numpy as np
print("Presentacion codigos en python")

c=[6,7,5]
d=[4,5,8]
sum=c[0]+d[1]
res=d[0]+c[1]
cruz=np.cross(c,d)
punto=np.dot(d,c)
divicion=np.divide(c,d)
print("Valor de la suma",sum,"Valor de la resta",res)
print("Valor producto punto",punto,"Valor producto cruz",cruz)
print("Valor divicion",divicion)

