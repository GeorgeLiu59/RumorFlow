#eulers.py
import numpy as np
import matplotlib.pyplot as plt
import sys
# Define parameters
a = 0.5 #lambda s
b = 0.1 #lambda r
c = 0.1 #sigma s
d = 0.1 #omega r
x = 0.95 #importance value
# Define initial conditions
U0 = 1950
S0 = 40
R0 = 10
I0 = 0
# Define time parameters
t0 = 0
T = 0.30 # Total time
dt = 0.0001 # Time step
num_steps = int(T / dt) # Number of time steps
# Initialize arrays to store results
U = np.zeros(num_steps)
S = np.zeros(num_steps)
R = np.zeros(num_steps)
I = np.zeros(num_steps)
time = np.zeros(num_steps)
8
# Set initial conditions
U[0] = U0
S[0] = S0
R[0] = R0
I[0] = I0
time[0] = t0
# Euler’s method
for i in range(1, num_steps):
dU_dt = -U[i-1]*S[i-1] - U[i-1]*R[i-1]
dS_dt = a*U[i-1]*S[i-1] + (c-d-x)*S[i-1]*R[i-1]
dR_dt = b*U[i-1]*S[i-1] + (d-c-x)*S[i-1]*R[i-1]
dI_dt = (1-a)*U[i-1]*S[i-1] + (1-b)*U[i-1]*R[i-1] +
(x+x)*S[i-1]*R[i-1]
if (dI_dt < 400):
print(i*dt)
sys.exit()
U[i] = U[i-1] + dt * dU_dt
S[i] = S[i-1] + dt * dS_dt
R[i] = R[i-1] + dt * dR_dt
I[i] = I[i-1] + dt * dI_dt
time[i] = time[i-1] + dt
# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time, U, label=’U’)
plt.plot(time, S, label=’S’)
plt.plot(time, R, label=’R’)
plt.plot(time, I, label=’I’)
plt.xlabel(’Time’)
plt.ylabel(’Population’)
plt.title(’Populations of U,S,R,I vs Time’)
plt.legend()
plt.grid(True)
ax = plt.gca()
ax.set_xlim([0, 0.30])
plt.show()