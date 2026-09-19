def flip_name(s):
    if len(s) == 1:
        return s
    return flip_name(s[1:]) + s[0]

input("flip_name recurses on s[1:] then attached s[0] at the end. Press enter")
print("flip_name(Maya) = ", flip_name("Maya")) 

name = input("Enter a name (try Riya or Dev): ")
print("Flip_name('" + name + "') = ", flip_name(name))