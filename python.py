import numpy as np
import matplotlib.pyplot as plt

# Define the matrix with quadratic functions
matrix = [
    [lambda x: 2*x**2 + 3*x + 6, lambda x: 2*x**2 + 3*x + 3, lambda x: 3*x**2 + 4*x + 7],
    [lambda x: 3*x**2 + 4*x + 7, lambda x: 2*x**2 - 6*x + 8, lambda x: x**2 + 5*x + 2],
    [lambda x: x**2 - x + 3, lambda x: 4*x**2 + 3*x + 1, lambda x: 5*x**2 - 2*x + 4]
]

# Linear approximation of the functions around x = 0
linear_approx_matrix = []
for row in matrix:
    linear_row = []
    for func in row:
        x0 = 0  # we will linearize around x = 0
        linear_approx = lambda x, f=func: f(x0) + (x - x0) * (lambda x: 6*x + 3)(x0)  # f(x0) + f'(x0)(x - x0)
        linear_row.append(linear_approx)
    linear_approx_matrix.append(linear_row)

# Calculate the angles using sin-1(log(constant))
constants = [
    [6, 3, 7],
    [7, 8, 2],
    [3, 1, 4]
]
angles = np.arcsin(np.log(constants))

# Plotting the lines
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Center point
center = [0, 0, 0]

# Plot each line
for i in range(3):
    for j in range(3):
        # Extract linear function
        func = linear_approx_matrix[i][j]
        # Generate points
        x_vals = np.linspace(-10, 10, 100)
        y_vals = func(x_vals)
        z_vals = np.zeros_like(x_vals)
        
        # Apply angle transformation
        angle = angles[i][j]
        x_rot = x_vals * np.cos(angle) - z_vals * np.sin(angle)
        z_rot = x_vals * np.sin(angle) + z_vals * np.cos(angle)
        
        ax.plot(x_rot, y_vals, z_rot, label=f'Line {i+1},{j+1}')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()
