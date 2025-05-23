p1 = input("Enter New Password: ")
p2 = input("Confirm Password: ")
if p1==p2:
    print("Password Changed Successfully")
elif p1.casefold()==p2.casefold():
    print("Error: Check Password Case")
else:
    print("Passwords do not Match")
