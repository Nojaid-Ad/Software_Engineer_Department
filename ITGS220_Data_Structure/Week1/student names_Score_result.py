# List of student names
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

# List of student scores
scores = [85, 62, 75, 90, 55]

# Define the passing threshold
passing_threshold = 70

# Print the scores and results of each student
for i in range(len(students)):
    if scores[i] >= passing_threshold:
        result = "Pass"
    else:
        result = "Fail"
    print(f"Student {students[i]} - Score: {scores[i]}, Result: {result}")
