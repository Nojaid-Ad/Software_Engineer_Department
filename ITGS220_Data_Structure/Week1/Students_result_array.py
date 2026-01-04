# Define the array to store Boolean values for pass or fail
pass_fail = []

# Suppose we have 5 students and their average scores
average_scores = [85, 62, 75, 90, 55]

# Define the passing threshold
passing_threshold = 70

# Iterate through each student's average score
for score in average_scores:
    # Check if the score is above the passing threshold
    if score >= passing_threshold:
        pass_fail.append(True)  # True indicates pass
    else:
        pass_fail.append(False)  # False indicates fail

# Print the pass/fail status of each student
for i, status in enumerate(pass_fail):
    if status:
        print(f"Student {i+1}: Pass")
    else:
        print(f"Student {i+1}: Fail")
