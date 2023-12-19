str_manip = input("Enter a sentence: ")

length_of_str = len(str_manip)
print("Length of str_manip:", length_of_str)

last_letter = str_manip[-1]

modified_str = str_manip.replace(last_letter, '@')

print("Modified string:", modified_str)

last_three_backwards = str_manip[-3:][::-1]
print("Last 3 characters backwards:", last_three_backwards)

five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:", five_letter_word)
