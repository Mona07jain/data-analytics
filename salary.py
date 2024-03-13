# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:34:58 2024

@author: hp
"""

x=[1.1,1.3,1.5,2,2.2,2.9,3,3.2,3.2,3.7,3.9,4,4,4.1,4.5,4.9,5.1,5.3,5.9,6,6.8,7.1,7.9,8.2,8.7,9,9.5,9.6,10.3,10.5]
y=[39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]
xy=[]
x_square=[]
sum=0
for i in range(len(x)):
    sum=sum+x[i]
    xy.append(x[i]*y[i])
    x_square.append((x[i])**2)

sum1=0
for j in range(len(xy)):
    sum1=sum1+xy[j]


sum2=0
for k in range(len(x_square)):
    sum2=sum2+x_square[k]
 

sum3=0
for l in range(len(y)):
    sum3=sum3+y[l]

m=(((len(x)*sum1)-(sum*sum3))/((len(x)*sum2)-(sum**2)))
print("slope :"+str(m))
c=((sum3-(m*sum))/(len(x)))
print("intercept :"+str(c))


x=[1.1,1.3,1.5,2,2.2,2.9,3,3.2,3.2,3.7,3.9,4,4,4.1,4.5,4.9,5.1,5.3,5.9,6,6.8,7.1,7.9,8.2,8.7,9,9.5,9.6,10.3,10.5]
a=[39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]
p=[]
error=[]
mod_error=[]
square_error=[]
percentage_error=[]
for d in range(len(x)):
    p.append((m*(x[d]))+c)
for i in range(len(a)):
    error.append(a[i]-p[i])
    mod_error.append(abs(a[i]-p[i]))
    square_error.append((a[i]-p[i])**2)
    percentage_error.append(abs((a[i]-p[i])/a[i])*100)



sum=0
for n in range(len(mod_error)):
    sum=sum+mod_error[n]

mae=sum/len(a)
print('mae:'+str(mae))   

sum=0
for o in range(len(square_error)):
    sum=sum+square_error[o]

mse=sum/len(a)
print('mse(model):'+str(mse))   

sum=0
for p in range(len(percentage_error)):
    sum=sum+percentage_error[p]

mape=sum/len(a)
print('mape:'+str(mape))
      

a=[39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]
sum=0
for i in range(len(a)):
    sum=sum+a[i]
average=sum/len(a)

e=[]
square_error1=[]

for i in range(len(a)):
    e.append(a[i]-average)
    square_error1.append((a[i]-average)**2)

sum=0
for k in range(len(square_error1)):
    sum=sum+square_error1[k]
    

m=(sum/(len(a)))
r2=1-(mse/m)
print('r2 :'+str(r2))

    