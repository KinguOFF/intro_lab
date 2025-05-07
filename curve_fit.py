import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Select a pendulum .csv file", filetypes=[("CSV files", "*.csv")]
)

if not file_path:
    print("No file selected.")
    exit()

df = pd.read_csv(file_path)
time = df.iloc[:, 0].values

col_index = int(input("Enter the column index for acceleration (e.g., 2 for 3rd column): "))
acc_y = df.iloc[:, col_index].values

L = float(input("Enter the length of the pendulum (in meters): "))

start_time = 3.0
end_time = time[-1] - 5.0
mask = (time >= start_time) & (time <= end_time)
time_filtered = time[mask]
acc_y_filtered = acc_y[mask]

def damped_pendulum_model(t, A, beta, omega, phase, offset):
    return A * np.exp(-np.abs(beta) * t) * np.sin(omega * t + phase) + offset

A0 = (np.max(acc_y_filtered) - np.min(acc_y_filtered)) / 2
beta0 = 0.1
omega0 = np.sqrt(9.8 / L)
guess = [A0, beta0, omega0, 0.0, np.mean(acc_y_filtered)]

params, _ = curve_fit(damped_pendulum_model, time_filtered, acc_y_filtered, p0=guess)
A, beta, omega, phase, offset = params
g_est = omega**2 * L

plt.figure(figsize=(10, 5))
plt.scatter(time_filtered, acc_y_filtered, s=5, label="y-acceleration", alpha=0.6)
plt.plot(
    time_filtered,
    damped_pendulum_model(time_filtered, *params),
    color="red",
    label=f"Fit: g ≈ {g_est:.2f} m/s², β ≈ {abs(beta):.3f}"
)

equation_str = (
    r"$a_y(t) = {:.2f} \cdot e^{{-{:.3f}t}} \cdot \sin({:.3f}t + {:.2f}) + {:.2f}$"
).format(A, abs(beta), omega, phase, offset)

plt.text(
    0.05, 0.95, equation_str,
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='top',
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8)
)

plt.xlabel("Time (s)")
plt.ylabel("y-Acceleration (m/s²)")
plt.title(f"{os.path.basename(file_path)}")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
