import numpy as np # ready for future addition
def power_output(ws: float,
                 interp_method: str, 
                 # Cp = 0.4, 
                 # air_density = 1.225,
                 # rotor_diameter = 100, 
                 rated_P = 15, 
                 cut_in_ws =  3,
                 rated_ws = 11,
                 cut_out_ws = 25
                 ):
    """
    function that calculate the power output
    """
    # interpolation method
    if interp_method not in ("linear", "cubic"): # the input check shall be in the main script, but just in case also here
        raise ValueError("interp_method must be 'linear' or 'cubic'")
    elif interp_method == "cubic":
        g = ws**3/rated_ws**3
    else:
        # default is linear interpolation
        g = (ws - cut_in_ws) / (rated_ws - cut_in_ws)

    # ready for exact power calculation with full formula
    # area = np.pi * rotor_diameter**2 / 4 

    if ws < cut_in_ws or ws > cut_out_ws:
        return 0.0 # turbine stopped
    elif ws >= rated_ws and ws < cut_out_ws:
        return rated_P # rated condition
    else:
        return g * rated_P # subrated condition, power output interpolated

    return power