import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ----------------------------
# Bezier Class
# ----------------------------
class Bezier:
    @staticmethod
    def TwoPoints(t, P1, P2):
        return (1 - t) * P1 + t * P2

    @staticmethod
    def Points(t, points):
        return [Bezier.TwoPoints(t, points[i], points[i + 1]) for i in range(len(points) - 1)]

    @staticmethod
    def Point(t, points):
        while len(points) > 1:
            points = Bezier.Points(t, points)
        return points[0]

    @staticmethod
    def Curve(t_values, points):
        return np.array([Bezier.Point(t, points) for t in t_values])


# ----------------------------
# Initial Points Function
# ----------------------------
def create_control_points(p1_y):
    return np.array([
        [100, 10],
        [150, p1_y],       # P1 is adjustable
        [190, 50],
        [190, 100],
        [190, 100],
        [190, 150],
        [150, 190],
        [100, 190],
        [100, 190],
        [50, 190],
        [10, 150],
        [10, 100],
        [10, 100],
        [10, 50],
        [50, 10],
        [100, 10]
    ])


# ----------------------------
# Drawing Function
# ----------------------------
def draw(p1_y):
    ax.clear()
    points = create_control_points(p1_y)
    t_points = np.linspace(0, 1, 100)

    # Create curves
    full_curve = Bezier.Curve(t_points, points)
    curve1 = Bezier.Curve(t_points, points[0:4])
    curve2 = Bezier.Curve(t_points, points[4:8])
    curve3 = Bezier.Curve(t_points, points[8:12])
    curve4 = Bezier.Curve(t_points, points[12:16])

    # Plot Bezier curves
    ax.plot(curve1[:, 0], curve1[:, 1], "b", linewidth=3, label="4 Cubic Beziers")
    ax.plot(curve2[:, 0], curve2[:, 1], "b", linewidth=3)
    ax.plot(curve3[:, 0], curve3[:, 1], "b", linewidth=3)
    ax.plot(curve4[:, 0], curve4[:, 1], "b", linewidth=3)

    ax.plot(full_curve[:, 0], full_curve[:, 1], "m", linewidth=2, label="Single Bezier (15 pts)")

    # Plot control polygon
    ax.plot(points[:, 0], points[:, 1], "ro--", markersize=5, linewidth=1, label="Control Points")

    # Draw reference circle
    circle = plt.Circle((100, 100), 90, color='gray', alpha=0.4, label="True Circle")
    ax.add_patch(circle)

    # Setup axes
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 200)
    ax.set_aspect('equal')
    ax.grid(True)

    # Move legend outside
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=8)

    fig.canvas.draw_idle()


# ----------------------------
# Plot Setup
# ----------------------------
fig, ax = plt.subplots(figsize=(7, 7))
plt.subplots_adjust(bottom=0.25, right=0.75)  # extra room for slider and legend
draw(10)

# ----------------------------
# Slider
# ----------------------------
ax_slider = plt.axes([0.25, 0.1, 0.45, 0.03])
p1_slider = Slider(ax_slider, 'P1 Y', 0, 100, valinit=10)

def update(val):
    draw(p1_slider.val)

p1_slider.on_changed(update)

plt.show()
