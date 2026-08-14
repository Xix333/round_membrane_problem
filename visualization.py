import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jn_zeros

# Налаштування параметрів (напр. вузлова мода m=1, кутова: n=2)
m = 2
n = 10
a = 1.0  # Умовний радіус мембрани
root = jn_zeros(m, n)[-1]  # n-й нуль функції Бесселя порядку m

# Створення некруглої, "щільної" сітки 
r = np.linspace(0, a, 107)
theta = np.linspace(0, 2*np.pi, 203)
r_mesh, theta_mesh = np.meshgrid(r, theta)

# Декартові координати
X = r_mesh * np.cos(theta_mesh)
Y = r_mesh * np.sin(theta_mesh)

# Розрахунок амплітуди: U(r, phi) = J_m(k_mn * r) * cos(m * phi)
Z = jv(m, root * r_mesh / a) * np.cos(m * theta_mesh)

# Візуалізація
fig = plt.figure(figsize=(12, 6))

# Поверхня
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)
ax1.set_title(f'Форма коливань мембрани (m={m}, n={n})')
ax1.set_zlim(-1.17, 1.17)
ax1.axis('off')

# Контурний графік 
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=37, cmap='viridis')
ax2.set_aspect('equal')
ax2.set_title('Вузлові лінії (контурний графік)')
plt.colorbar(surf, ax=ax2, shrink=0.8)

plt.tight_layout()
plt.savefig('membrane_mode_1_2.png', dpi=300, bbox_inches='tight')
plt.show()