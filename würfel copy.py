import random

def roll_die():
    number = random.randint(1, 6)
    return number

number_of_rolls = int(2)

result_total = 0
for _ in range(number_of_rolls):
    roll_result = roll_die()
    print("Roll:", roll_result)
    result_total += roll_result
print("Result total:", result_total)
