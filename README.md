ATM Simulator - Python

Overview
This is a simple ATM simulator program written in Python. It allows users to check their account details, deposit money, withdraw cash, and check their balance using a PIN authentication system.

Features
- PIN Authentication: Users must enter the correct PIN to access the ATM services.
- Account Details: Displays the account holder's name and masked account number.
- Deposit Money: Allows deposits in denominations of 100, 200, or 500.
- Withdraw Money: Allows withdrawals in denominations of 100, 200, or 500, ensuring sufficient balance.
- Balance Check: Displays the user's current account balance.
- Retry Mechanism: Users get three attempts to enter the correct PIN before the card is locked.
- User-Friendly Navigation: Options to continue or exit transactions easily.

How It Works
1. Insert Your Card
2. Enter Your PIN (3 attempts allowed, after which the card is locked)
3. Choose an option:
   - (1) View Account Details
   - (2) Deposit Money
   - (3) Withdraw Money
   - (4) Check Balance
4. Perform Transactions
5. Option to Continue or Exit

## Usage
- The program starts by prompting the user to enter their PIN.
- If the PIN is correct, the user can perform banking operations.
- Transactions are executed based on the selected option.
- The user is given the choice to continue or exit after each transaction.
- If the PIN is entered incorrectly three times, the account is locked.

Example

Enter Your PIN Number: xxxx

1. Account Details
2. Deposit
3. Withdraw
4. Balance

Please Select The Form of Mode Do You Want: 2
Place The Cash (only 100/200/500) to Deposit: 500
500/- Amount Is Credited To Your Bank Account 
and Your Current Balance is 9500/-

You Want To Continue Press '0' or Press Any Key To Exit:
