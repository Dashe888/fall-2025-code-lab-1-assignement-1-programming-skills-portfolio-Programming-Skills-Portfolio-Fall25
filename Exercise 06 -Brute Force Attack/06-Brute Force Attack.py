CORRECT_PASSWORD = "12345"
# Start a variable for the user's attempt.
user = ""
# LOOP: Keep running as long as the user input is WRONG.
while user != CORRECT_PASSWORD:
   # Get the password attempt.
    user = input("ENTER PASSWORD: ")
   # If the attempt is still WRONG:
    if user != CORRECT_PASSWORD:
        # Print a warning.
        print("AW nah we got a hacker")
# When correct, exit the loop and grant access.
print ("Access Granted, you still suspicous tho")        


