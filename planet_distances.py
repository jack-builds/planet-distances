import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
au = [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.2, 30.1]

fig, ax = plt.subplots(figsize=(11,6))
bars = ax.bar(planets, au, color=["#b0b0b0","#e8c97a","#4a90d9","#d96a4a","#d9b06a","#e0d090","#8fd0d9","#4a6ad9"])
ax.set_title("Distance of the 8 Planets from the Sun")
ax.set_ylabel("Distance (AU, 1 AU = ~150 million km)")
for b, v in zip(bars, au):
    ax.text(b.get_x()+b.get_width()/2, v+0.4, f"{v} AU", ha="center")
ax.set_ylim(0, 33)
plt.tight_layout()
plt.savefig("planet_distances.png", dpi=150)
print("Saved planet_distances.png")
