def is_power4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return is_power4(n // 4)
    return False

input("is_power4 divides by 4 - n==1 return the True remainder returns False. Press enter")
print(" is_power4(16) = ", is_power4(16))
print(" is_power4(12) = ", is_power4(12))

n = int(input("Enter a number (try 64 or 48): "))
guess = input("What is is_power4(" + str(n) + ")? ")
print(" is_power4(" + str(n) + ") = ", is_power4(n), "your guess: ", guess)
