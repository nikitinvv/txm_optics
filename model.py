import matplotlib.pyplot as plt
import numpy as np

# take from the spreadsheet
na_tip = 1.48*1e-3
na_opening = 1.39*1e-3
d_con = 287
s_con = 0
inner_con = 850*1e-3
outer_con = 1000*1e-3

energy = 8000
lamd = 1240/energy
dr_zp = 50
zp_size = 150
na_zp = 1000*lamd/(2*dr_zp)
dof_zp = 2*lamd/(2*(na_zp/1000)**2)/1000
f_zp = zp_size*dr_zp/(1000*lamd)

# for plotting
na_zp /= 1000
zp_size /= 1000

x = np.linspace(-f_zp, d_con)
y = np.tan(na_tip)*x
x += s_con
plt.plot(x, y, 'r', label='Condenser NA')
plt.plot(x, -y, 'r')

x = np.linspace(-f_zp, d_con)
y = np.tan(na_opening)*x
x += s_con
plt.plot(x, y, 'r')
plt.plot(x, -y, 'r')


x = np.linspace(-f_zp, 0)
y = np.tan(na_zp)*x
plt.plot(x, y, 'b', label='ZP NA')
plt.plot(x, -y, 'b')


x = [-f_zp, -f_zp]
y = [-f_zp*np.tan(na_zp), f_zp*np.tan(na_zp)]
# plt.plot(x,y,'r')
plt.text(x[0]-10, y[0]-0.08, 'ZP')


x = [d_con+20, d_con+20]
y = [-inner_con/2, inner_con/2]
plt.plot(x, y, 'y')
plt.text(x[0]-10, y[0]-0.04, 'inner')
plt.text(x[0]-20, y[1]+0.05, 'condenser')
x = [d_con+60, d_con+60]
y = [-outer_con/2, outer_con/2]
plt.plot(x, y, 'y', label='Condenser inner/outer plane')
plt.text(x[0]-10, y[0]-0.04, 'outer')


x = [-f_zp, -f_zp]
y = [-zp_size/2, zp_size/2]
plt.plot(x, y, 'g', label='ZP plane')


plt.text(-50, -0.3, f'{na_tip=},{na_opening=}, {inner_con=},{outer_con=} ')
plt.text(-50, -0.4, f'{na_zp=:03f}, {f_zp=}, {zp_size=}')
plt.xlabel('mm')
plt.ylabel('mm')
plt.grid()
plt.legend()
plt.title(f'{energy}keV, {dr_zp}nm ZP')
plt.show()
