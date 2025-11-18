import sys
if len(sys.argv) == 4:
    script_name = sys.argv[0]
    principal = sys.argv[1]
    rate = sys.argv[2]
    time = sys.argv[3]
else:
    script_name = sys.argv[0]
    principal = 10000
    rate = 10
    time = 2
print("Invalid input using default values")
simple_interest = (float(principal) * float(rate) * float(time)) / 100
print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", simple_interest)
