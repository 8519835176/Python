positive_sum = 0
negative_sum = 0
positive_count = 0
negative_count = 0

print("Enter -1 to exit…")

# Continuously read numbers from the user
while True:
    number = int(input("Enter the number: "))
    
    if number == -1:
        break
    
    if number > 0:
        positive_sum += number
        positive_count += 1
    elif number < 0:
        negative_sum += number
        negative_count += 1

# Calculate the averages
if positive_count > 0:
    positive_average = positive_sum / positive_count
else:
    positive_average = 0

if negative_count > 0:
    negative_average = negative_sum / negative_count
else:
    negative_average = 0

# Print the results
print(f"The average of negative numbers is: {negative_average}")
print(f"The average of positive numbers is: {positive_average}")
