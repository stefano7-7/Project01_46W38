import wind_utilities as wutil
import numpy as np
import matplotlib.pyplot as plt

# power = [];
wind_speeds = np.linspace(0,30,1000)
interp_method = input("choose [linear, cubic]: ").strip().lower()

if interp_method not in ("linear", "cubic"):
        raise ValueError("interp_method must be 'linear' or 'cubic'")

power_linear = None
power_cubic = None

# power with both mnethods
if interp_method == "linear":
    power_linear = [wutil.power_output(ws, "linear") for ws in wind_speeds]
    print(power_linear)
else:
    power_cubic = [wutil.power_output(ws, "cubic") for ws in wind_speeds]    
    print(power_cubic)


# power curve plot
plt.figure(figsize=(8,5))
if power_linear is not None:
    plt.plot(wind_speeds, power_linear, label="Linear interp", linewidth=2)
if power_cubic is not None:
    plt.plot(wind_speeds, power_cubic, label="Cubic interp", linewidth=2, linestyle="--")

# Abbellimenti
plt.title("Wind Turbine Power Curve")
plt.xlabel("Wind Speed [m/s]")
plt.ylabel("Power Output [MW]")
plt.legend()
plt.grid(True)

# Mostriamo il grafico
plt.show()
