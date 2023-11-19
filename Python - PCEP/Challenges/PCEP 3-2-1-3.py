secret_number = 0
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

secret_number = int(input("pick a number:"))
while secret_number != 777:
        print("Ha, ha! You're stuck in my loop")
        if secret_number < 777:
            print("Think greater!")
        else:
            print("Think smaller!")
        secret_number = int(input("pick a number:"))
    
print("Well done, muggle! you are free now")