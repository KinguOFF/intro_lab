# Gera os graficos do tracker e aplica media movel aos a_x gerados pelo tracker

import pandas as pd
import matplotlib.pyplot as plt

file_path = input("Insira o local dos dados, e.g /home/massas.txt \n")
data = pd.read_csv(
    file_path, sep="\t", skiprows=2, names=["t", "x", "v_x", "a_x"], engine="python"
)

data = data.dropna()
data["a_x"] = data["a_x"] / 100

data["a_x_smooth"] = data["a_x"].rolling(window=5, center=True).mean()

plt.figure(figsize=(10, 5))
plt.plot(data["t"], data["a_x"], label="Tracker a_x", color="blue", alpha=0.5)
plt.plot(
    data["t"],
    data["a_x_smooth"],
    label="Media Movel a_x",
    linewidth=1,
    linestyle="dashed",
)
plt.plot(data["t"], data["v_x"], label="Tracker v_x", color="red", alpha=0.5)
plt.plot(data["t"], data["x"], label="Tracker x", color="black", alpha=0.5)
plt.xlabel("Tempo (s)")
plt.ylabel("Acel. (ms^-2), Vel (m^s-1), Pos (m)")
plt.legend()
plt.ylim(-10, 10)

plt.title("Tracker e Média Móvel")
plt.show()
