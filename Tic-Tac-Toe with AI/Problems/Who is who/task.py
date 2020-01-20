class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


char_type, char_value = input().split()
if getattr(Angel, char_type) == char_value:
    print('Angel')
elif getattr(Demon, char_type) == char_value:
    print('Demon')
else:
    print('No match')
