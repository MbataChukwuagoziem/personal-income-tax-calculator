# Name: Mbata Chukwuagoziem Daniel
# Matric Number: BU24SEN1004
# Course: COS 201
# Program: Personal Income Tax Calculator (2009)

def tax_calculator(filing_type, annual_income):
    # Tax limits and percentages based on filing status
    tax_table = {
        0: [  # Single filer
            (8350, 0.10),
            (33950, 0.15),
            (82250, 0.25),
            (171550, 0.28),
            (372950, 0.33),
            (10**12, 0.35)
        ],
        1: [  # Married filing jointly / Qualifying widow(er)
            (16700, 0.10),
            (67900, 0.15),
            (137050, 0.25),
            (208850, 0.28),
            (372950, 0.33),
            (10**12, 0.35)
        ],
        2: [  # Married filing separately
            (8350, 0.10),
            (33950, 0.15),
            (68525, 0.25),
            (104425, 0.28),
            (186475, 0.33),
            (10**12, 0.35)
        ],
        3: [  # Head of household
            (11950, 0.10),
            (45500, 0.15),
            (117450, 0.25),
            (190200, 0.28),
            (372950, 0.33),
            (10**12, 0.35)
        ]
    }

    total_tax = 0
    last_limit = 0

    for upper_bound, percent in tax_table[filing_type]:
        if annual_income > upper_bound:
            taxable_part = upper_bound - last_limit
            total_tax += taxable_part * percent
            last_limit = upper_bound
        else:
            taxable_part = annual_income - last_limit
            total_tax += taxable_part * percent
            break

    return total_tax


# -------- Program Execution Starts Here --------
print("Select Filing Status")
print("0 - Single")
print("1 - Married Filing Jointly / Qualifying Widow(er)")
print("2 - Married Filing Separately")
print("3 - Head of Household")

user_status = int(input("Enter your filing status (0 - 3): "))
user_income = float(input("Enter your taxable income ($): "))

result = tax_calculator(user_status, user_income)

print(f"Your total personal income tax is: ${result:.2f}")
