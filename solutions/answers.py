from problems.rand_prob import RandomProblem as rand
from formula.circuit import Circuit

class Answers:
    
    def answers_for_problem_one():
        
        answer_key = {}
        given = rand.generate_problem_one()
        answer_key["given"] = given
        
        
        # ANSWERS
        answer_key['res_total'] = Circuit.solve_series_resistance(
            given_res = [given["res_one"], given["res_two"], given["res_three"]])
        answer_key['current_total'] = Circuit.solve_current(
            voltage = given["voltage"], 
            resistance = answer_key['res_total'])
        
        # Current is constant through resistors in series.
        answer_key['current_one'] = answer_key['current_total']
        answer_key['current_two'] = answer_key['current_total']
        answer_key['current_three'] = answer_key['current_total']
        
        answer_key['voltage_one'] = Circuit.solve_voltage(
            current = answer_key['current_one'],
            resistance = given["res_one"])
        
        answer_key['voltage_two'] = Circuit.solve_voltage(
            current = answer_key['current_two'],
            resistance = given["res_two"])
        
        answer_key['voltage_three'] = Circuit.solve_voltage(
            current = answer_key['current_three'],
            resistance = given["res_three"])
        
        volt_total = Circuit.sum_in_float(
            answer_key['voltage_one'], answer_key['voltage_two'], answer_key['voltage_three'])
        
        pow_one = Circuit.solve_power(
            voltage = answer_key['voltage_one'], current = answer_key['current_one'])
        pow_two = Circuit.solve_power(
            voltage = answer_key['voltage_two'], current = answer_key['current_two'])
        pow_three = Circuit.solve_power(
            voltage = answer_key['voltage_three'], current = answer_key['current_three'])
        
        pow_total = Circuit.sum_in_float(pow_one, pow_two, pow_three)
        
        print("Total Res:")
        print(answer_key['res_total'])
        print("Total Current:")
        print(answer_key['current_total'])
        
        print("Power:")
        print(pow_one)
        print(pow_two)
        print(pow_three)
        print(pow_total)
        
        print("Current:")
        print(answer_key['current_one'])
        print(answer_key['current_two'])
        print(answer_key['current_three'])
        
        print("Voltage:")
        print(answer_key['voltage_one'])
        print(answer_key['voltage_one'])
        print(answer_key['voltage_one'])
        print(volt_total)
        
        print("Given:")
        print(given["voltage"])
        print(given["res_one"])
        print(given["res_two"])
        print(given["res_three"])
        return answer_key
        
        
        
        