ones_and_zeros_list = []
final_number = "0."
multiplier = 1 
number_input = float(input("Type in your decimal number lower than zero: "))


while multiplier >= (1/729):
    if number_input >= (float(multiplier * (2 / 3))):
        ones_and_zeros_list.append("2")
        number_input -= float(multiplier * (2 / 3))

    elif number_input >= (float(multiplier * (1 / 3))):
        ones_and_zeros_list.append("1")
        number_input -= float(multiplier * (1 / 3))
    else:
        ones_and_zeros_list.append("0")
    multiplier *= 1/3
    print(multiplier)
    
for i in range(0, len(ones_and_zeros_list)):
    final_number += ones_and_zeros_list[i]

print(ones_and_zeros_list)
print(f'your number in base two is {final_number}')

#this is basically the same thing as the base two converter, but i added the cases in which the program will add the number "2" to the list.
