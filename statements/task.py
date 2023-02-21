
ln1 = input("Line1:")
ln2 = input ("Line2:")
n1=len(ln1)
n2=len(ln2)
result = n1 == n2

i=0
found_str = ""
while i < n1 and result:
    #ln1_char = ln1[i]
    #ln2_char = ln2[i]
    is_ln1_char_found = found_str.__contains__(ln1[i])
    is_ln2_char_found = found_str.__contains__(ln2[i])

    if not(is_ln1_char_found) and not(is_ln2_char_found):
        print("Both characters not processed yet, let's check them")
        #Add characters from both strings to the string which contains already processed characters
        found_str += ln1[i] + ln2[i]

        ln1_char_indexes = [i]
        ln2_char_indexes = [i]
        j = i + 1
        while j < n1:
            if ln1[j] == ln1[i]: #ln1_char:
                ln1_char_indexes.append(j)
            if ln2[j] == ln2[i]: #ln2_char:
                ln2_char_indexes.append(j)
            j += 1

        print("List of indexes of line1 character", ln1[i], ":", ln1_char_indexes)
        print("List of indexes of line2 character", ln2[i], ":", ln2_char_indexes)
        print("Compare indexes of chars", ln1[i], "and", ln2[i], "inside their strings")
        result = ln1_char_indexes == ln2_char_indexes

    elif is_ln1_char_found and not(is_ln2_char_found):
        print("Only character from 1st line already processed. Comparison fails")
        result = False
    elif not(is_ln1_char_found) and is_ln2_char_found:
        print("Only character from 2nd line already processed. Comparison fails")
        result = False
    else:
        print("Both characters already processed, which is OK. Do nothing at this iteration")
     

    i += 1

print(result)