from ctypes import Union
import settings as set
from tkinter import messagebox

class Circuit:
    
    def solve_series_resistance(given_res: list) -> float:
        res_total = float(round(sum(given_res), set.rounded))
        return res_total
    
    def solve_current(voltage: float, resistance: float) -> float:
        current = float(round(voltage / resistance, set.rounded))
        return current
    
    def solve_voltage(current: float, resistance: float) -> float:
        voltage = float(round(current * resistance, set.rounded))
        return voltage
    
    def solve_resistance(voltage: float, current: float) -> float:
        resistance = float(round(voltage / current , set.rounded))
        return resistance
    
    def solve_power(voltage: float = None, current: float = None, resistance : float = None) -> float:
        if voltage == None:
            power = float(round((current ** 2) * resistance, set.rounded))
        elif current == None:
            power = float(round((voltage ** 2) / resistance, set.rounded))
        elif resistance == None:
            power = float(round(voltage * current, set.rounded))
        else:
            messagebox.showerror("Something is wrong.", 'Error: There seems to be a problem in solving the circuit.\nPlease do message/inform the admin and exit this game. Thank you.!')
        return power
        
    def sum_in_float(*args: tuple[float]) -> float:
            value = float(round(sum(args), set.rounded))
            return value
        
        