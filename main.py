"""
an array of wind speeds is created covering a range from zero to high winds, typical for onshore in Europe
an interpolation method for the sub-rated part of the power curve is chosen by the User
a function for power output is called
a power curve is printed and also plotted
a comparison in terms of time of execution (efficincy) is made between two power output functions 
"""

import wind_utilities as wutil
import numpy as np
import matplotlib.pyplot as plt
import time

# power = [];
no_points = 1000
wind_speeds = np.linspace(0,30,no_points)
interp_method = input("choose [linear, cubic]: ").strip().lower()

if interp_method not in ("linear", "cubic"):
        raise ValueError("interp_method must be 'linear' or 'cubic'")

# inizialization of the variables 
power_linear = None
power_cubic = None

# calling the function calculating the power 
# with both interp methods according to User choice
if interp_method == "linear":
    power_linear = [wutil.power_output(ws, "linear") for ws in wind_speeds]
    print(power_linear)
else:
    power_cubic = [wutil.power_output(ws, "cubic") for ws in wind_speeds]    
    print(power_cubic)


## efficiency comparison
# basic function
timeStart = time.time()
power_basicFunction = [wutil.power_output(ws, interp_method) for ws in wind_speeds]
timeFinish = time.time()

# print only some values, avoiding 0
no_points = len(power_basicFunction)
step = max(1, no_points // 10)         
print(power_basicFunction[1::step])    
# basic function execution time
print(f"base function execution time: {(timeFinish - timeStart):.5f} s")

# supposedly improved function
timeStart = time.time()
power_vectorizedFunction = [wutil.power_output_vectorized(ws, interp_method) for ws in wind_speeds]
timeFinish = time.time()
print(f"vectorized function execution time: {(timeFinish - timeStart):5f} s")

# power curve plot for sanity check
plt.figure(figsize=(8,5))
plt.plot(wind_speeds, power_basicFunction, label="basic func", linewidth=2)
plt.plot(wind_speeds, power_vectorizedFunction, label="vectoriz func", linewidth=2, linestyle="--")

plt.title("Wind Turbine Power Curve")
plt.xlabel("Wind Speed [m/s]")
plt.ylabel("Power Output [MW]")
plt.legend()
plt.grid(True)

# show chart & let User close it manually
plt.show()