import time

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
print("Let's replace the middle number,", hat_list[2] , "with an integer number entered by you")
print("The current list we have is: ", hat_list)
time.sleep(1)

numberSwitch = int(input("Type a number:"))
print("The number to be replaced  is ", hat_list[2])
hat_list[2] = numberSwitch

print("And the new list is:")
print("Ta-da!")
time.sleep(1)
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.
print("\nNow we will delete the last element of the list")
print("The list before removing the last element is:", hat_list)
print("Deleting: ", hat_list[-1])
del hat_list[-1]
print("The list without that element: ", hat_list)

# Step 3: write a line of code that prints the length of the existing list.
print("Let's see how long is this list:", len(hat_list))
