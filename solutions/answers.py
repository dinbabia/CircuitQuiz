from problems.rand_prob import RandomProblem as rand
from formula.circuit import Circuit

class Answers:
    
    def answers_for_problem_one():
        
        data = {}
        given = rand.generate_problem_one()
        
        
        # ANSWERS
        res_total = Circuit.solve_series_resistance(
            given_res = [given["res_one"], given["res_two"], given["res_three"]])
        current_total = Circuit.solve_current(
            voltage = given["voltage"], 
            resistance = res_total)
        
        # Current is constant through resistors in series.
        curr_one = current_total
        curr_two = current_total
        curr_three = current_total
        
        volt_one = Circuit.solve_voltage(
            current = curr_one,
            resistance = given["res_one"])
        
        volt_two = Circuit.solve_voltage(
            current = curr_two,
            resistance = given["res_two"])
        
        volt_three = Circuit.solve_voltage(
            current = curr_three,
            resistance = given["res_three"])
        
        volt_total = Circuit.sum_in_float(volt_one, volt_two, volt_three)
        
        pow_one = Circuit.solve_power(voltage = volt_one, current = curr_one)
        pow_two = Circuit.solve_power(voltage = volt_two, current = curr_one)
        pow_three = Circuit.solve_power(voltage = volt_three, current = curr_one)
        
        pow_total = Circuit.sum_in_float(pow_one, pow_two, pow_three)
        
        print("Total Res:")
        print(res_total)
        print("Total Current:")
        print(current_total)
        
        print("Power:")
        print(pow_one)
        print(pow_two)
        print(pow_three)
        print(pow_total)
        
        print("Current:")
        print(curr_one)
        print(curr_two)
        print(curr_three)
        
        print("Voltage:")
        print(volt_one)
        print(volt_two)
        print(volt_three)
        print(volt_total)
        
        print("Given:")
        print(given["voltage"])
        print(given["res_one"])
        print(given["res_two"])
        print(given["res_three"])
        return given
        
        
        
        