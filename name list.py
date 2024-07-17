# Define the names string and the desired order
names = "apple,carrot,beans,dear"
order = "a"

# Split the names string into a list of names
names_list = names.split(',')

# Sort the list based on the order specified
if order == "a":
    sort = sorted(names_list)  # Sort in ascending order
elif order == "d":
    sort = sorted(names_list, reverse=True)  # Sort in descending order
else:
    print("Order not valid. Use 'a' for ascending or 'd' for descending.")
    sort = names_list  # No sorting if the order is not valid

# Print the sorted list
print(sort)
