user_int, empt, rev = input("Enter Palindrome Words: ").lower().replace(" ", ""), [], []
for i in user_int:
    empt.append(i)
    rev.insert(0, i)
    # if i == " ":
    #     empt.remove(" ")
    #     rev.remove(" ")
empt_l, rev_l = ''.join(map(str, empt)), ''.join(map(str, rev))
print(f"{user_int}{' = Palindrome' if empt_l == rev_l else ' = Not Palindrome'}")
