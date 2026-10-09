# Program: Bug Hunt
# Purpose: Calculates the sum of numbers from 1 to 5 using a while loop.

count = 1
total = 0

# BUG: Missing colon (:) at the end of the while loop header line. Fixed by adding :.
# BUG: Off-by-one condition (count < 5 stopped at 4, giving total 10 instead of 15). Fixed by changing condition to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: TypeError when concatenating a string and integer with +. Fixed by using an f-string to format total.
print(f"Sum of 1 to 5 is: {total}")