n = int(input("Enter number of students: "))

for i in range(n):
    score = float(input(f"Enter score for student {i+1}: "))

    if score >= 60:
        print("Strong Performance")
    else:
        print("Weak Performance")
