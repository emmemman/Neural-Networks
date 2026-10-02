import matplotlib.pyplot as plt

def load_xy(path):
    xs, ys = [], []
    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.split()
            xs.append(float(parts[0]))
            ys.append(float(parts[1]))
    return xs, ys

xc, yc = load_xy("check_correct.dat")
xw, yw = load_xy("check_wrong.dat")

plt.scatter(xc, yc, s=10, marker="o", label="Correct")
plt.scatter(xw, yw, s=25, marker="x", label="Wrong")
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Check set: Correct vs Wrong")
plt.grid(True)
plt.legend()
plt.show()
