import numpy as np
import matplotlib.pyplot as plt

# Input
print("Use z (example: z, z**2, np.sin(z))")
func = input("Enter function f(z): ")

# Grid
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# Complex plane
Z_complex = X + 1j * Y

# Function
F = eval(func, {"z": Z_complex, "np": np})

# Take magnitude (height)
Z = np.abs(F)

# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(
    X, Y, Z,
    cmap='viridis',   # color shading 🔥
    edgecolor='none'
)

# Color bar (like your image)
fig.colorbar(surface, ax=ax, shrink=0.5)

# Labels
ax.set_xlabel('Real Axis')
ax.set_ylabel('Imaginary Axis')
ax.set_zlabel('|f(z)|')

ax.set_title('3D Complex Surface')

plt.show()
