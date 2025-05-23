# Reset-Password

This Python program checks whether a newly entered password and its confirmation match, ensuring consistency and helping avoid password entry errors.

## 💡 Features

- Accepts a new password and confirmation input from the user.
- Checks for:
  - **Exact match** → Accepts and confirms password.
  - **Case-insensitive match** → Warns the user about case mismatch.
  - **Mismatch** → Informs the user that the passwords do not match.

## 📋 Program Logic

1. User is prompted to enter a new password (`p1`).
2. User is prompted to confirm the password (`p2`).
3. The program checks:
   - If `p1 == p2`: prints “Password Changed Successfully”.
   - If `p1.casefold() == p2.casefold()`: prints “Error: Check Password Case”.
   - Else: prints “Passwords do not Match”.

## ▶️ Example

Enter New Password: SecurePass123
Confirm Password: securepass123
Output: Error: Check Password Case


## 🧪 Run the Program

```bash
python reset-password.py


