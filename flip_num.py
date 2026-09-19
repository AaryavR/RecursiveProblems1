def flip_num(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flip_num(num // 10) 
    return last * pow(10, len(str(rest))) + rest 

input("Flip Numer peels the last digit with % 10 then recurses on // 10. Press Enter ")
print(" flip_num(123) = ", flip_num(123))

n = int(input("Enter a number (try 789 or 1234): "))
guess = input("What is flip_number(" + str(n) + ")? ")
print(" flip_num(" + str(n) + ") = ", flip_num(n), " your guess: ", guess) 