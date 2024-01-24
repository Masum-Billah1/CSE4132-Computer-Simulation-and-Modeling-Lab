from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

a = [100.0]
b = [50.0]
c = [0.0]
t = dt = 0.01
k1 = 0.008
k2 = 0.002
total_time = 5.0
step = int(5/0.01)
time = [t]

figure, ax = plt.subplots()
ax.set_xlim(0, (total_time / dt))
ax.set_ylim(0, max(a[-1],b[-1]))

(line_a,) = ax.plot([], [], label="a")
(line_b,) = ax.plot([], [], label="b")
(line_c,) = ax.plot([], [], label="c")

def animate(x):
    global t, total_time
    if t < total_time:
        print(a[-1]," ",b[-1]," ",c[-1])
        a_new = (a[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt)
        b_new = (b[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt)
        c_new = c[-1] + (2 * k1 * a[-1] * b[-1] - 2 * k2 * c[-1]) * dt

        b.append(b_new)
        a.append(a_new)
        c.append(c_new)
        time.append(t)
        t+=dt;

    line_a.set_data(range(len(a)), a)
    line_b.set_data(range(len(b)), b)
    line_c.set_data(range(len(c)), c)

animation = FuncAnimation(figure, animate, frames = 1, interval = 1)


plt.legend()
plt.title("Chemical Reactor")
plt.xlabel("Time (s)")
plt.ylabel("Mole/vol (s)")
plt.show()
