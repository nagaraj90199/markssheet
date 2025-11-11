import sys

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

marks = [80, 85, 90, 75, 70]

if len(sys.argv) == 6:
    marks = [float(m) for m in sys.argv[1:6]]
else:
    print("No input given — using default marks:", marks)

avg = sum(marks) / 5
grade = get_grade(avg)

print(f"\nAverage Marks = {avg:.2f}")
print(f"Grade = {grade}")
