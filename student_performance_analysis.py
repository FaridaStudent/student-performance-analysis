n = int(input("Enter number of students: "))

for i in range(1, n + 1):
    score = float(input(f"Enter score for student {i}: "))

    if score >= 60:
        print("Strong Performance")
    else:
        print("Weak Performance")
