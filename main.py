import wind_utilities as wutil
import numpy as np
import matplotlib.pyplot as plt

# power = [];
wind_speeds = np.linspace(0,30,50)
#interp_method = input("choose [linear, cubic]: ").strip().lower()
#if interp_method not in ("linear", "cubic"):
    #raise ValueError("interp_method must be 'linear' or 'cubic'")

# for ws in wind_speeds:
# power = wutil.power_output(ws, interp_method )
# print("wind speeds are: {wind_speeds}")
# print("power output: {power}")


# power with both mnethods
powers_linear = [wutil.power_output(ws, "linear") for ws in wind_speeds]
powers_cubic  = [wutil.power_output(ws, "cubic") for ws in wind_speeds]

# power curve plot
plt.figure(figsize=(8,5))
plt.plot(wind_speeds, powers_linear, label="Linear interp", linewidth=2)
plt.plot(wind_speeds, powers_cubic, label="Cubic interp", linewidth=2, linestyle="--")

# Abbellimenti
plt.title("Wind Turbine Power Curve")
plt.xlabel("Wind Speed [m/s]")
plt.ylabel("Power Output [MW]")
plt.legend()
plt.grid(True)

# Mostriamo il grafico
plt.show()
