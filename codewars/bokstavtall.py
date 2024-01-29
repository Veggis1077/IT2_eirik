def position(alphabet):
    return (ord(alphabet) - 96)


bokstaver = 'abcdefghijklmnopqrstuvwxyz'


def alphabet_position(text):
    tallstr = ''
    text = text.lower()

    for i in text:
        if i not in bokstaver:
            text = text.replace(i, '')
        else:
            tallstr = tallstr + str(position(i)) + ' '
    tallstr = tallstr.rstrip(tallstr[-1])

    return tallstr

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("utidtydk"))