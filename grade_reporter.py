# Program: Grade Reporter
# Purpose: Classifies student scores into letter grades, tracks pass/fail counts, and calculates the class average.

scores = [72, 45, 90, 61, 38]

# Initialize tracking variables
passes = 0
fails = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    total_score += score  # Accumulate total for average calculation
    
    # Determine letter grade based on score conditions
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    # Track pass/fail statistics
    if score >= 50:
        passes += 1
    else:
        fails += 1
        
    print(f"Score: {score} - Grade: {grade}")

# Calculate average rounded to 1 decimal place
average = round(total_score / len(scores), 1)

# Display summary results
print("-" * 25)
print(f"Passed: {passes}")
print(f"Failed: {fails}")
print(f"Average score: {average}")