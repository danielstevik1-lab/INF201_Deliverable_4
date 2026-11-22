""" -----Temperature conversion----- """

class Temperature():
    def __init__(self,value:float,unit:str,comp:str):
        self.value = float(value)
        self.unit = unit.lower()
        self.comp = comp.lower()

        if self.to_kelvin() < 0:
            raise ValueError("Temperature below absolute zero")
        elif self.unit not in ("k", "c", "f", "kelvin", "celsius", "farenheit"):
            raise ValueError("Enter valid unit. Valid units: kelvin/k, celsius/c or farenheit/f")


    def to_celsius(self)->float:
        """Converts kelvin or farenheit to celsius"""
        
        if self.unit in ("k","kelvin"):
            return self.value -273.15
        elif self.unit in ("f", "farenheit"):
            return (self.value-32)*(5/9)
        else:
            return self.value
        
          


    def to_farenheit(self)->float:
        """ Converts kelvin or celsius to farenheit"""
    
        if self.unit in("k", "kelvin"):
            return (self.value -273)*(9/5)+32
        elif self.unit in("c","celsius"):
            return (self.value *(9/5))+32
        else:
            return self.value
        
    

    def to_kelvin(self)->float:
        """ Converts celsius or farenheit to kelvin"""
        
        if self.unit in("c","celsius"):
            return self.value + 273.15
        elif self.unit in("f", "farenheit"):
            return (self.value-32)*(5/9) + 273.15
        else:
            return self.value          


    def comparison(self, temp_a, temp_b, comp)->str:
        """
        Takes to temperatures and a comarison operator, returns the result.
        Logic: Check if tempA is 'operator' than tempB.
        Available comp-operators: ==, !=, <, <=,>, >=.
        """
        if comp == "==":
            return "Temperature A and B are the same!" if temp_a == temp_b else "Temperature A and B are not the same!"
            
        elif comp == "!=":
            return "Temperature A is different from Temperature B." if temp_a != temp_b else "Temperature A is the same as Temperature B." 
            
        elif comp == "<":
            return "Temperature A is lower than Temperature B" if temp_a < temp_b else "Temperature A is higher than Temperature B"
        elif comp == "<=":
            return "Temperature A is equal or lower than Temperature B" if temp_a <= temp_b else "Temperature A is higher than Temperature B"
        elif comp == ">":
            return "Temperature A is higher than Temperature B" if temp_a > temp_b else "Temperature A is lower than Temperature B"
        elif comp == ">=":
            return "Temperature A is equal or higher than Temperature B" if temp_a >= temp_b else "Temperature A is lower than Temperature B"
        else:
            raise ValueError("Enter valid operators: ==, !=, <, <=, >, >=")



    def __repr__(self)->str:
        return f"Temperature({self.value},'{self.unit}')"


    def __str__(self)->str:
        return f"{self.value:.2f}°{self.unit}"        


temp1= Temperature(300,"K")
temp2 = Temperature(98,"f")
temp3 = Temperature(-27.0,"c")
print(f"{temp3.to_celsius():.2f}")