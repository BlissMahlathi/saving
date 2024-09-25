import numpy as np
import matplotlib.pyplot as plt

# Define the functions as lambda functions
functions = [
    [lambda x: 2*x**2 + 3*x + 6, lambda x: 2*x**2 + 3*x + 3, lambda x: 2*x**2 + 3*x + 7],
    [lambda x: 3*x**2 + 4*x + 6, lambda x: 3*x**2 + 4*x + 7, lambda x: 3*x**2 + 4*x + 8],
    [lambda x: 3*x**2 - 6*x + 6, lambda x: 3*x**2 - 6*x + 7, lambda x: 3*x**2 - 6*x + 8]
]

# Point of linearization
x0 = 1

# Linear approximations and normalizations
linear_approximations = []
norm_factors = []

for row in functions:
    lin_row = []
    norm_row = []
    for f in row:
        f_prime = lambda x: 4*x + 3 if '2x' in str(f) else (6*x + 4 if '3x' in str(f) else 0)
        f_prime_at_x0 = f_prime(x0)
        f_at_x0 = f(x0)
        linear_approx = lambda x, f_prime=f_prime_at_x0, f=f_at_x0: f + f_prime * (x - x0)
        lin_row.append(linear_approx)
        norm_row.append(max(abs(f_prime_at_x0), abs(f_at_x0)))
    linear_approximations.append(lin_row)
    norm_factors.append(norm_row)

# Calculate angles
angles = [[np.arcsin(np.log((norm_row))) for norm_row in norm_factors_row] for norm_factors_row in norm_factors]

# Plotting
fig, ax = plt.subplots()
for i, row in enumerate(linear_approximations):
    for j, lin_approx in enumerate(row):
        theta = angles[i][j]
        x_vals = np.linspace(-10, 10, 400)
        y_vals = lin_approx(x_vals)
        ax.plot(x_vals * np.cos(theta), y_vals * np.sin(theta), label=f'Line {i},{j}')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.grid(True)
plt.title("Radial Pattern of Linear Approximations")
plt.show()
