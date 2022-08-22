from random import *
from typing import Dict



class RandomProblem:
    
    def random_number(min: float, max: float) -> float:
        return float(randint(min, max))
    
    def generate_problem_one() -> Dict:
        given = {}
        given["voltage"] = RandomProblem.random_number(min = 115, max = 130)
        given["res_one"] = RandomProblem.random_number(min = 20, max = 40)
        given["res_two"] = RandomProblem.random_number(min = 20, max = 40)
        given["res_three"] = RandomProblem.random_number(min = 20, max = 40)
        return given