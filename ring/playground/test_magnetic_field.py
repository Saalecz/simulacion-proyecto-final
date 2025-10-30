import magpylib as magpy
import numpy as np
from magpylib.func import cylinder_field
import matplotlib.pyplot as plt

# create the mesh for the area of a circle of radius 5 at z=2 and inside its perimeter
r = 5
z_plane = 2
num_points = 50000
theta = np.linspace(0, 2 * np.pi, int(np.sqrt(num_points)))
radii = np.linspace(0, r, int(np.sqrt(num_points)))
r_grid, theta_grid = np.meshgrid(radii, theta)
x = r_grid * np.cos(theta_grid)
y = r_grid * np.sin(theta_grid)
z = np.full_like(x, z_plane)    
points = np.column_stack((x.ravel(), y.ravel(), z.ravel()))

# plot the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Points in Circle at z=2')
plt.show()

# define cylinder parameters
cylinder_center = (0, 0, 0)
cylinder_axis = (0, 0, 1)
cylinder_radius = 1
cylinder_height = 1
cylinder_magnetization = (0, 0, 1000)  # Magnetization along z-axis
# compute magnetic field at the defined points
B_field = cylinder_field(
    field="B",
    observers=points,
    dimensions=(cylinder_radius, cylinder_height),
    positions=cylinder_center,
    polarizations=cylinder_magnetization,
)

# reshape B_field for easier handling
B_field_reshaped = B_field.reshape(x.shape[0], x.shape[1], 3)

#plot the magnitude of the magnetic field on the circle plane
B_magnitude = np.linalg.norm(B_field_reshaped, axis=2)
plt.figure()
plt.contourf(x, y, B_magnitude, levels=50, cmap='viridis')
plt.colorbar(label='Magnetic Field Magnitude (T)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Magnetic Field Magnitude on Circle at z=2')
plt.axis('equal')
plt.show()