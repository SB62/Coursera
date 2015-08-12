hrs = float(raw_input("Enter Hours:"))
rte = float(raw_input("Enter Pay Rate:"))
if hrs <= 40:
    x = hrs
    gross = (x * rte)
    
elif hrs > 40:
    y = hrs - 40
    x = 40
    gross = (x * rte) + (y * (1.5 * rte))
    
print gross 