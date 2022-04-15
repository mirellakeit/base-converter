ones_and_zeros_list = []                                                     #Creates a list, in which I'll store the 0's and 1's later, 
                                                                             #in order.
    
final_number = "0."                                                          #Creates a String starting with '0.', as I'll add the 0's and 
                                                                             #1's later via the aforementioned list.

multiplier = 1                                                               #Creates the number I'll use in the first loop

number_input = float(input("Type in your decimal number lower than zero: ")) #It creates an input, which will store the User's number, 
                                                                             #and automatically converts it to a float

while multiplier >= (1/64):
    if number_input >= (float(multiplier * (1 / 2))):                       #This loop basically works like this: It'll firstly check if the user's input
        ones_and_zeros_list.append("1")                                     #is greater or equal a half, in which case, it'll add the number "1" as the
        number_input -= float(multiplier * (1 / 2))                         #first element of the list. If the input happens to be lower than 0.5, it will
    else:                                                                   #add a "0" to the list. at the end of those ifs and elses it will divide
        ones_and_zeros_list.append("0")                                     #the multiplier variable by two. 
    multiplier *= 1/2                                                       #I chose the loop to end when multiplier >= 1/64, because I had to settle a
                                                                            #limit, otherwise the program would run forever in some cases like the
                                                                            #input 0.3. I chose 1/2^6, but this is completely arbitrary.
                                                                            #(I'll add more information as to why i decided to put the loop like this
                                                                            #in this file's description.)
    
    
for i in range (0, len(ones_and_zeros_list)):                               #Now, since i've previously put 0's and 1's in a list, in order of placement on
    final_number += ones_and_zeros_list[i]                                  #the base 2 system, I'll just add those 0's and 1's to a string that starts 
                                                                            #with "0." so, if the list is ["0", "1", "0", "0", "1"] the result will be
                                                                            #the string 0.01001 


print(f'your number in base two is {final_number}')                         #prints the result
