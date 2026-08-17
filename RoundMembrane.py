import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jn_zeros
from matplotlib.backends.backend_qtagg import FigureCanvas


A = 1.0



class RoundMembrane(FigureCanvas):
    def __init__(self, m, n):
        self.fig = plt.figure(figsize=(12, 6))
        super().__init__(self.fig)
        self.ax1 = self.fig.add_subplot(121, projection='3d')
        self.ax2 = self.fig.add_subplot(122)
        self.m = m
        self.n = n
        self.root = jn_zeros(self.m, self.n)[-1]
        self.r = np.linspace(0, A, 107)
        self.theta = np.linspace(0, 2*np.pi, 203)
        self.r_mesh, self.theta_mesh = np.meshgrid(self.r, self.theta)
        self.X = self.r_mesh * np.cos(self.theta_mesh)
        self.Y = self.r_mesh * np.sin(self.theta_mesh)
        self.Z = jv(self.m, self.root * self.r_mesh / A) * np.cos(self.m * self.theta_mesh)
        self.surf = self.ax1.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='none', alpha=0.9)
        plt.colorbar(self.surf, ax=self.ax2, shrink=0.8)
        

    def visualize(self):
        self.ax1.cla()
        self.ax2.cla()

        
        self.ax1.set_title(f'Форма коливань мембрани (m={self.m}, n={self.n})')
        #self.ax1.set_zlim(-1.17, 1.17)
        self.ax1.axis('off')

        self.surf = self.ax1.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='none', alpha=0.9)
        self.contour = self.ax2.contourf(self.X, self.Y, self.Z, levels=37, cmap='viridis')
        self.ax2.set_aspect('equal')
        self.ax2.set_title('Вузлові лінії (контурний графік)')

        
        

        plt.tight_layout()
        self.draw()


    def refreshData(self):
        self.root = jn_zeros(self.m, self.n)[-1]
        self.r = np.linspace(0, A, 107)
        self.theta = np.linspace(0, 2*np.pi, 203)
        self.r_mesh, self.theta_mesh = np.meshgrid(self.r, self.theta)
        self.X = self.r_mesh * np.cos(self.theta_mesh)
        self.Y = self.r_mesh * np.sin(self.theta_mesh)
        self.Z = jv(self.m, self.root * self.r_mesh / A) * np.cos(self.m * self.theta_mesh)
    