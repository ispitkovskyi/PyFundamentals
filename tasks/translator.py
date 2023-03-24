
'''Any vowel (glasniy zvuk) in a word will be substituted with "g". 
   Examples:  dog -> dgg;  cat -> cgt; oops -> ggps
'''
def translate(phrase):
    transation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transation = transation + "G"
            else:
                transation = transation + "g"
        else:
            transation = transation + letter
    return transation


print(translate(input("Enter a phrase to translat: ")))