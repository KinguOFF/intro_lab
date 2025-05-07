import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk

# Hide the main tkinter window
Tk().withdraw()

file_path = filedialog.askopenfilename(
    title="Select a text file",
    filetypes=[("Text files", "*.txt")]
)

if not file_path:
    print("No file selected.")
    exit()

with open(file_path, "r") as f:
    data = [float(line.strip()) for line in f if line.strip()]

plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Data from File")
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
