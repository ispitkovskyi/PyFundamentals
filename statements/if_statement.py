
is_mail = True
is_tall = False

#if is_mail or is_tall:
if is_mail and is_tall:
    print("You are a tall male")
elif is_mail and not(is_tall):
    print("Your are a short male")
elif not(is_mail) and is_tall:
    print("Your are a not a male, but are tall")
else:
    print("You are not a male and not tall")