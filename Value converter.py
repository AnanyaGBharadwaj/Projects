def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "m": 1, "km": 0.001, "cm": 100, "mm": 1000, "inch": 39.3701, "ft": 3.28084, "yd": 1.09361, "mile": 0.000621371
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "kg": 1, "g": 1000, "mg": 1e6, "lb": 2.20462, "oz": 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "F" and to_unit == "K":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32
    return value  
print("Length:", length_converter(10, "m", "ft"), "feet")
print("Weight:", weight_converter(5, "kg", "lb"), "pounds")
print("Temperature:", temperature_converter(100, "C", "F"), "Fahrenheit")
print("Distance:",length_converter(1245,"m","km"),"kilometer")
