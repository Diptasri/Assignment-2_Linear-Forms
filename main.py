
import matplotlib.pyplot as plt
Ax = 2
Ay = 0
Bx = 0
By = -2
Cx = 0
Cy = 0
Dx = 2
Dy = 2

plt.figure(1)
plt.xlim(0 , 2.5)
plt.ylim(-2 , 0.5)
plt.scatter([Ax, Bx], [Ay, By], color= 'r', marker = 'o')
plt.text(Ax, Ay + 0.5, '({},{})'.format(Ax, Ay))
plt.text(Bx, By + 0.5, '({},{})'.format(Bx, By))
plt.plot([Ax, Bx], [Ay, By])
#plt.title("Linear_form 2")
plt.xlabel("X- Axis")
plt.ylabel("Y- Axis")
plt.grid(True)
plt.show()

plt.figure(2)
plt.xlim(0 , 2.5)
plt.ylim(0 , 2.5)
plt.scatter([Cx, Dx], [Cy, Dy], color= 'r' , marker = 'o')
plt.text(Cx, Cy + 0.5, '({},{})'.format(Cx, Cy))
plt.text(Dx, Dy + 0.5, '({},{})'.format(Dx, Dy))
plt.plot([Cx, Dx], [Cy, Dy])
#plt.title("Linear_form 2")
plt.xlabel("X- Axis")
plt.ylabel("Y- Axis")
plt.grid(True)
plt.show()
