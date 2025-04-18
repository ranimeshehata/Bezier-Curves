# Bézier Curve Visualization

This project visualizes Bézier curves and demonstrates how to approximate a circle using four cubic Bézier curves. The visualization is interactive, allowing users to adjust a control point dynamically using a slider.

## Features

- **Bézier Curve Construction**: Implements Bézier curve calculations using Python.
- **Circle Approximation**: Approximates a circle using four cubic Bézier curves.
- **Interactive Slider**: Adjust the position of a control point to see how the curve changes in real time.
- **Matplotlib Visualization**: Displays the curves, control points, and a reference circle for comparison.

## How It Works

1. **Control Points**: The control points for the Bézier curves are defined in the `create_control_points` function. One of the control points (`P1`) is adjustable via a slider.
2. **Curve Calculation**: The `Bezier` class provides static methods to calculate Bézier curves for given control points and parameter values.
3. **Drawing**: The `draw` function plots the Bézier curves, control points, and a reference circle.
4. **Interactive Slider**: A slider allows users to adjust the `P1` control point's y-coordinate, dynamically updating the visualization.

![21010531_drawing](https://github.com/user-attachments/assets/c209c644-8382-4eb4-b600-47ff8ce1fd6f)
