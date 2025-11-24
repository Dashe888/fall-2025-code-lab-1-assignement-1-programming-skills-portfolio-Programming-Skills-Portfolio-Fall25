# List of names.
names = [ "jake", "Sam", "Zeke", "Ron", "Dave", "Ian"] 
# The name to find. 
Target = 'Sam' 
# Flag to track if the name is found.
Found = False
search = (f"Looking for '{Target}' in the list: {names} \n")
print(search)
# LOOP: Check every name one by one.
for name in names:
   # If match is found:
    if name == Target:
        # Print success, set flag to True, and STOP checking the rest of the list.
        print(f"HOORAY YOU FOUND {Target} IN THE LIST YIPPE!!")
        found = True
        break
    # If no match in this step:
    else:
        # Print a message about the check.
        print(f"Checked {names} who's that?")
else:
    # AFTER LOOP: Print "not in the list" if the loop finished without finding the name.
    print(f"\nResult: {Target} ts guy is not in the list")        
    