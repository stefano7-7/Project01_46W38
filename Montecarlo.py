"""
calculation of pi value using Montecarlo method
randomly generated points with seed fixed for reproduceability
"""
import numpy as np

no_runs = 15
no_points =1000

def estimate_PI(no_points: int, seed = None):
    rng = np.random.default_rng(seed)
    x_randomly_gen_point = rng.random(no_points)
    y_randomly_gen_point = rng.random(no_points)
    points_quadrant = []
    points_quadrant = (x_randomly_gen_point**2 + \
            y_randomly_gen_point**2 ) <= 1 
    inside_count = np.sum(points_quadrant)
    return 4 * inside_count/no_points

pi_esteem = []
for i in range(no_runs):
    pi_esteem.append(estimate_PI(no_points))
print(f"The estimated value of pi is: {np.mean(pi_esteem):.4f}")