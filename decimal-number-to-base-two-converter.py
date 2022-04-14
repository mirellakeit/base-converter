ones_and_zeros_list = []
final_number = "0."
multiplier = 1 
number_input = float(input("Type in your decimal number lower than zero: "))
half_the_multiplier = float(multiplier * (1/2))

while multiplier >= (1/64):
    if number_input >= (float(multiplier * (1 / 2))):
        ones_and_zeros_list.append("1")
        number_input -= float(multiplier * (1 / 2))
    else:
        ones_and_zeros_list.append("0")
    multiplier *= 1/2
    print(multiplier)
    
for i in range (0, len(ones_and_zeros_list)):
    final_number += ones_and_zeros_list[i]

print(ones_and_zeros_list)
print(f'your number in base two is {final_number}')