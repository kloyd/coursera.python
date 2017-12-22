def computepay(hours, rate):
    if (hours > 40):
        regHours = 40
        overHours = hours - 40
    else:
        regHours = hours
        overHours = 0

    pay = regHours * rate + overHours * rate * 1.5

    return pay

hrs = input("Enter Hours:")
hours = float(hrs)
rte = input("Enter Rate:")
rate = float(rte)
p = computepay(hours, rate)
print(p)
