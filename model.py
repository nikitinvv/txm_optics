import matplotlib.pyplot as plt
import numpy as np

na_tip = 1.48*1e-3
na_opening = 1.39*1e-3
d_con = 287
f_zp = 72.58
na_zp = 1.24*1e-3
inner_con = 850*1e-3
outer_con = 1000*1e-3
zp_size = 180*1e-3


x = [0,d_con]
y = [0,d_con*np.tan(na_tip)]

plt.plot(x,y,'r',label='Condenser NA')

x = [0,d_con]
y = [0,-d_con*np.tan(na_tip)]
plt.plot(x,y,'r')

x = [0,d_con]
y = [0,d_con*np.tan(na_opening)]

plt.plot(x,y,'r')

x = [0,d_con]
y = [0,-d_con*np.tan(na_opening)]
plt.plot(x,y,'r')


x = [d_con,d_con]
y = [-d_con*np.tan(na_tip),d_con*np.tan(na_tip)]
plt.plot(x,y,'r')



x = [0,-f_zp]
y = [0,-f_zp*np.tan(na_zp)]
plt.plot(x,y,'b',label='ZP NA')
x = [0,-f_zp]
y = [0,f_zp*np.tan(na_zp)]
plt.plot(x,y,'b')
x = [-f_zp,-f_zp]
y = [-f_zp*np.tan(na_zp),f_zp*np.tan(na_zp)]


x = [0,-f_zp]
y = [0,-f_zp*np.tan(na_tip)]

plt.plot(x,y,'r')

x = [0,-f_zp]
y = [0,-f_zp*np.tan(na_opening)]
plt.plot(x,y,'r')

x = [0,-f_zp]
y = [0,f_zp*np.tan(na_tip)]

plt.plot(x,y,'r')

x = [0,-f_zp]
y = [0,f_zp*np.tan(na_opening)]
plt.plot(x,y,'r')


x = [-f_zp,-f_zp]
y = [-f_zp*np.tan(na_zp), f_zp*np.tan(na_zp)]
#plt.plot(x,y,'r')
plt.text(x[0]-10,y[0]-0.08,'ZP')


x = [d_con+20,d_con+20]
y = [-inner_con/2, inner_con/2]
plt.plot(x,y,'y')
plt.text(x[0]-10,y[0]-0.04,'inner')
plt.text(x[0]-20,y[1]+0.05,'condenser')
x = [d_con+60,d_con+60]
y = [-outer_con/2, outer_con/2]
plt.plot(x,y,'y',label='Condenser inner/outer plane')
plt.text(x[0]-10,y[0]-0.04,'outer')


x = [-f_zp,-f_zp]
y = [-zp_size/2, zp_size/2]
plt.plot(x,y,'g', label= 'ZP plane')


# d_szp = 3441
# x = [-f_zp,-d_szp-f_zp]
# y = [f_zp*np.tan(na_tip),0]
# plt.plot(x,y,'r')




plt.text(-50,-0.3,f'{na_tip=},{na_opening=}, {inner_con=},{outer_con=} ')
plt.text(-50,-0.4,f'{na_zp=:03f}, {f_zp=}, {zp_size=}')
plt.xlabel('mm')
plt.ylabel('mm')
plt.grid()
plt.legend()
plt.title('10keV setup, 50nm ZP')
plt.show()









