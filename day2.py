bank = [
    [
        [
            ["C101", "Rahul", "Savings", 85000],
            ["C102", "Anita", "Current", 150000],
            ["C103", "Kiran", "Loan", 500000]
        ],
        [
            ["C104", "Sneha", "Savings", 95000],
            ["C105", "Vikram", "Current", 275000],
            ["C106", "Meena", "Loan", 750000]
        ]
    ],

    [
        [
            ["C201", "Arjun", "Savings", 120000],
            ["C202", "Pooja", "Current", 325000],
            ["C203", "Ramesh", "Loan", 900000]
        ],
        [
            ["C204", "Priya", "Savings", 45000],
            ["C205", "Amit", "Current", 185000],
            ["C206", "Divya", "Loan", 650000]
        ]
    ],

    [
        [
            ["C301", "Nikhil", "Savings", 78000],
            ["C302", "Kavya", "Current", 240000],
            ["C303", "Suresh", "Loan", 1000000]
        ],
        [
            ["C304", "Neha", "Savings", 135000],
            ["C305", "Rohan", "Current", 410000],
            ["C306", "Asha", "Loan", 550000]
        ]
    ]
]

# 1. Print Rahul's complete record.
print(bank[0][0][0])

# 2. Print Anita's account type.
print(bank[0][0][1][2])

# 3. Print Kiran's loan amount.
print(bank[0][0][2][3])

# 4. Print Sneha's customer ID.
print(bank[0][1][0][0])

# 5. Print Vikram's balance.
print(bank[0][1][1][3])

# 6. Print Meena's complete record.
print(bank[0][1][2])

# 7. Print Arjun's customer ID.
print(bank[1][0][0][0])

# 8. Print Pooja's name.
print(bank[1][0][1][1])

# 9. Print Ramesh's account type.
print(bank[1][0][2][2])

# 10. Print Priya's balance.
print(bank[1][1][0][3])

# 11. Print Amit's account type.
print(bank[1][1][1][2])

# 12. Print Divya's customer ID.
print(bank[1][1][2][0])

# 13. Print Nikhil's account type.
print(bank[2][0][0][2])

# 14. Print Kavya's balance.
print(bank[2][0][1][3])

# 15. Print Suresh's loan amount.
print(bank[2][0][2][3])

# 16. Print Neha's name.
print(bank[2][1][0][1])

# 17. Print Rohan's complete record.
print(bank[2][1][1])

# 18. Print Asha's account type.
print(bank[2][1][2][2])

# 19. Print all customers in Bank 1, Branch 1.
print(bank[0][0])

# 20. Print all customers in Bank 1, Branch 2.
print(bank[0][1])

# 21. Print all customers in Bank 2, Branch 1.
print(bank[1][0])

# 22. Print all customers in Bank 2, Branch 2.
print(bank[1][1])

# 23. Print all customers in Bank 3, Branch 1.
print(bank[2][0])

# 24. Print all customers in Bank 3, Branch 2.
print(bank[2][1])

# 25. Print all branches of Bank 1.
print(bank[0])

# 26. Print all branches of Bank 2.
print(bank[1])

# 27. Print all branches of Bank 3.
print(bank[2])

# 28. Print the first customer from every bank's first branch.
print(bank[0][0][0])
print(bank[1][0][0])
print(bank[2][0][0])

# 29. Print the second customer from every bank's second branch.
print(bank[0][1][1])
print(bank[1][1][1])
print(bank[2][1][1])

# 30. Print the loan amount of the last customer in Bank 3, Branch 2.
print(bank[2][1][2][3])