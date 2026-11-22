""" -----Temperature conversion----- """

class Temperature():
    def __init__(self,value,unit):
        self.value = float(value)
        self.unit = unit.lower()

        if self.to_kelvin() < 0:
            raise ValueError("Temperature below absolute zero")


    def to_celsius(self)->float:
        """Converts kelvin or farenheit to celsius"""
        
        if self.unit in ("k","kelvin"):
            return self.value -273.15
        elif self.unit in ("f", "farenheit"):
            return (self.value-32)*(5/9)
        elif self.unit in ("c", "celsius"):
            return self.value
        else:
            raise ValueError("Enter valid temperature units: k,f or c")
          


    def to_farenheit(self)->float:
        """ Converts kelvin or celsius to farenheit"""
    
        if self.unit in("k", "kelvin"):
            return (self.value -273)*(9/5)+32
        elif self.unit in("c","celsius"):
            return (self.value *(9/5))+32
        elif self.unit in("f", "farenheit"):
            return self.value
        else:
            raise ValueError("Enter valid temperature units: k,f or c")
    

    def to_kelvin(self)->float:
        """ Converts celsius or farenheit to kelvin"""
        
        if self.unit in("c","celsius"):
            return self.value + 273.15
        elif self.unit in("f", "farenheit"):
            return (self.value-32)*(5/9) + 273.15
        elif self.unit in ("k", "kelvin"):
            return self.value          
        else:
            raise ValueError("Enter valid temperature units: k,f or c")


    def __repr__(self)->str:
        return f"Temperature({self.value},'{self.unit}')"


    def __str__(self)->str:
        return f"{self.value:.2f}°{self.unit}"        


temp1= Temperature(300,"K")
temp2 = Temperature(98,"f")
temp3 = Temperature(-27.0,"c")
print(f"{temp3.to_celsius():.2f}")