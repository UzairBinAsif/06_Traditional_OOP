''' Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
    that returns the Fahrenheit value.'''

class TemperatureConverter:    # f = (c * 9/5) + 32
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return round(((c * 9/5) + 32), 2)

print(f'102°C = {TemperatureConverter.celsius_to_fahrenheit(100)}°F')