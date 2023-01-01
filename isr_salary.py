brackets = {
    6450: 10,
    9240: 14,
    14840: 20,
    20620: 31,
    42910: 35,
    1000000: 47,
}


def calc(salary: int) -> tuple:
    tax = 0
    pointer = 0
    for income, rate in brackets.items():
        if income < salary:
            tax += (income-pointer) * rate / 100
            pointer = income
        else:
            tax += (salary-pointer) * rate / 100
            break
    return salary-tax, tax
