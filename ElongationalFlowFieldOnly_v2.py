#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 22:31:48 2025

@author: Keshav
"""
"""
This code simulates an extensinal fluid flow-field within a Stokes Trap that is
used to trap particles suspended in the fluid. The Stokes Trap itslef is a 
micro-chip with 2 inlets and 2 outlets (for easy mass balance).
"""
import numpy as np
import matplotlib.pyplot as plt

# Extensional rate
epsilon_dot = 1.0

# Chip boundary conditions
low_bound = -2
high_bound = 2

# Interpolation points
int_num = 20

# Create grid of points
x = np.linspace(low_bound, high_bound, int_num) # lower and upper bound represent the chip boundaries (X - axis)
y = np.linspace(low_bound, high_bound, int_num) # lower and upper bound represent the chip boundaries (Y - axis)
X, Y = np.meshgrid(x, y)

# Velocity components for 2D uniaxial extensional flow
U = epsilon_dot * X      # velocity in x (stretching)
V = -epsilon_dot * Y     # velocity in y (compression)

# Plot velocity vectors
plt.figure(figsize=(6,6))
plt.quiver(X, Y, U, V, color='blue')
plt.title('2D Uniaxial Extensional Flow (Stokes Regime)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.show()