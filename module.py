import numpy as np 
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
from scipy import integrate

#набір даних speed
speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
print('Speed array:')
for i in range(12):
    print(speed[i], end='\t')
    
#1. time - вектор часу, створений за допомогою np.linspace
time=np.linspace(0, 11, 12) 

#2.	Виконайте вивід масиву часу time
print('\nTime array:')
for i in range(12):
    print(time[i], end='\t')

# 3. графік точок швидкості        
plt.plot(time, speed, 'go') 
   
# розмір області відображення 
plt.xlim([0, 11]) 
plt.ylim([0, 130]) 
plt.show()

# 4. Виконати інтерполяцію за допомогою interpld(kind='cubic') 
k=10000
new_time = np.linspace(0, 11, k)

# отримати функцію з 10 000 значеннями
new_speed = interpolate.interp1d(time, speed, kind='cubic')(new_time)

#графік отриманої функції.
plt.plot(new_time, new_speed, 'o-')
plt.xlim([0, 11]) 
plt.ylim([0, 130])
plt.show()

#5. Обчислити інтеграл для отримання інтерполяційної функції 
s=0
dt=11/k
for i in range(k):
    s+=new_speed[i]*dt
print ('інтеграл для інтерполяційної кубічної функції  = ',s)

#для kind='quadratic' отримати функцію з 10 000 значеннями
new_speed1 = interpolate.interp1d(time, speed, kind='quadratic')(new_time)
plt.plot(new_time, new_speed1, 'ro-')

plt.xlim([0, 11]) 
plt.ylim([0, 130])
plt.show()

#для kind='quadratic' обчислити інтеграл для отримання інтерполяційної функції s=0
dt=11/k
for i in range(k):
    s+=new_speed1[i]*dt
print ('інтеграл для інтерполяційної квадратичної функції  = ',s)
