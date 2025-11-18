import sys


if len(sys.argv) > 1:
    script_name=sys.argv[0]
    scores = sys.argv[1:]
    
    scores = [float(x) for x in scores]
else:
   
    scores = [50, 60, 70, 80, 90]
    print("No input given, using default scores:", scores)


total = sum(scores)
average = total / len(scores)


print("Scores:", scores)
print("Sum of Scores:", total)
print("Average of Scores:", average)

max=max(scores)
min=min(scores)

print("Minimum : ",min)
print("Maximum : ",max)
