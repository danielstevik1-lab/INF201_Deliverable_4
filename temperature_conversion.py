"""----- Temperature class -----"""
class Temperature:
    def __init__(self, value:float, unit:str)->None:
        """Initializing temperature class with variables connected to self."""
        self._value = float(value)
        self._unit = unit.lower()

        if self.to_kelvin() < -self.TOLERANCE:
            raise ValueError("Temperature below absolute zero.")
        elif self.unit not in ("k", "kelvin", "c", "celsius", "f", "fahrenheit"):
            raise ValueError("""
            Enter valid unit.
            Valid units:
             -Kelvin = 'k'
             -Celsius = 'c'
             -Farenhheit = 'f'""" )
        
    TOLERANCE = 1e-9        #Comparison tolerance     

    @property
    def value(self):
        return self._value
    @property
    def unit(self):
        return self._unit

    def to_celsius(self)->float:
        """Converts kelvin or fahrenheit to celsius"""       
        if self.unit in ("k","kelvin"):
            return self.value -273.15
        elif self.unit in ("f", "fahrenheit"):
            return (self.value-32)*(5/9)
        else:
            return self.value
            
              
    def to_fahrenheit(self)->float:
        """ Converts kelvin or celsius to fahrenheit"""  
        if self.unit in("k", "kelvin"):
            return (self.value -273.15)*(9/5)+32
        elif self.unit in("c","celsius"):
            return (self.value *(9/5))+32
        else:
            return self.value
            

    def to_kelvin(self)->float:
        """ Converts celsius or fahrenheit to kelvin"""          
        if self.unit in("c","celsius"):
            return self.value + 273.15
        elif self.unit in("f", "fahrenheit"):
            return (self.value-32)*(5/9) + 273.15
        else:
            return self.value

       
        
    def __eq__(self, other):
        """Checks if equal, =="""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return abs(self.to_kelvin() - other.to_kelvin())<=self.TOLERANCE

    def __ne__(self, other):
        """Checks if not equal, !="""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return not self.__eq__(other)

    def __lt__(self, other):
        """Checks if less than, <"""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self.to_kelvin() < other.to_kelvin() +self.TOLERANCE

    def __le__(self, other):
        """Checks if less or equal, <="""
        if not isinstance(other, Temperature):
            return NotImplemented
                
        return self.to_kelvin() <= other.to_kelvin() +self.TOLERANCE

    def __gt__(self, other):
        """Checks if greater than, >="""
        if not isinstance(other, Temperature):
            return NotImplemented
                
        return self.to_kelvin() > other.to_kelvin() - self.TOLERANCE

    def __ge__(self, other):
        """Checks if greater or equal, >="""
        if not isinstance(other, Temperature):
            return NotImplemented
                        
        return self.to_kelvin() >= other.to_kelvin() - self.TOLERANCE
    
    

    def convert_to(self,target_unit:str)->"Temperature":
        """Takes temperature of specific unit and converts it to a target unit"""
        target_unit = target_unit.lower()

        if target_unit in ("c", "celsius"):
            return Temperature(self.to_celsius(), "c")
        elif target_unit in("f", "fahrenheit"):
            return Temperature(self.to_fahrenheit(),"f")
        elif target_unit in ("k", "kelvin"):
            return Temperature(self.to_kelvin(),"k")
        else:
            raise ValueError("Invalid target unit")
    
    
    
    def __repr__(self)->str:
        return f"Temperature({self.value},'{self.unit}')"
        
    def __str__(self)->str:
        return f"{self.value:.2f} °{self.unit.upper()}"        
    
