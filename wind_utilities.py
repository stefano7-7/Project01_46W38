"""
function power_output()
function power_output_vectorized()
"""
import numpy as np # ready for future improvements
def power_output(ws: float,
                 interp_method: str, 
                 # Cp = 0.4, # ready for future addition
                 # air_density = 1.225, # ready for future addition
                 # rotor_diameter = 100, # ready for future addition
                 rated_P = 15, 
                 cut_in_ws =  3,
                 rated_ws = 11,
                 cut_out_ws = 25
                 ):
    """
    function that calculate the power output
    """
    # interpolation method
    if interp_method not in ("linear", "cubic"): 
        # the input check shall be in the main script, but just in case is checked here too
        raise ValueError("interp_method must be 'linear' or 'cubic'")
    elif interp_method == "cubic":
        g = ws**3/rated_ws**3
    else:
        # default is linear interpolation
        g = (ws - cut_in_ws) / (rated_ws - cut_in_ws)

    # ready for exact power calculation with full formula
    # area = np.pi * rotor_diameter**2 / 4 

    if ws < cut_in_ws or ws >= cut_out_ws:
        # turbine stopped
        return 0.0 
    elif ws >= rated_ws and ws < cut_out_ws:
        # rated condition
        return rated_P 
    else:
        # subrated condition, power output interpolated
        return g * rated_P 

    return power

def power_output_vectorized(ws: float,
                 interp_method: str, 
                 rated_P = 15, 
                 cut_in_ws =  3,
                 rated_ws = 11,
                 cut_out_ws = 25
                 ):
    """
    function that calculate the power output
    same as power_output(), but added vectorization and check of exceution time for comparison purposes
    """
    #
    ws_array = np.asarray(ws)

    # interpolation method
    if interp_method not in ("linear", "cubic"): # the input check shall be in the main script, but just in case also here
        raise ValueError("interp_method must be 'linear' or 'cubic'")
    elif interp_method == "cubic":
        g = ws_array**3/rated_ws**3
    else:
        # default is linear interpolation
        g = (ws_array - cut_in_ws) / (rated_ws - cut_in_ws)

    return np.where((ws_array < cut_in_ws) | (ws_array >= cut_out_ws), 0.0, \
                     np.where(ws_array < rated_ws, g * rated_P, \
                        rated_P))