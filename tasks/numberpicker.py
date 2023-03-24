
sample_num = input("Enter 3-digit number to guess:")
attempts = 10
sample_len = len(sample_num)

picked_mask = "x"
exit = False
while attempts < 10 and not(all_picked):
    attempts += 1
    temp_sample = sample_num
    guess_num = input("Enter your guess number:")

    if len(guess_num) != sample_len:
        print("Your number lenght doesn't match sample number")
        exit = True
    else:
        i = 0
        while i < sample_len:
            i += 1
            j = 0
            while j < sample_len:
                j += 1
                if guess_num[i] == sample_len[j] and i == j:
                    guess_num[i] = "picked "
                    sample_len[j] = picked_mask
                elif guess_num[i] == sample_len[j] and i != j:
    