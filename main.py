def main():
    lst = [
        'sh', 'gl', 'ch', 'ph', 'tr', 'br',
        'fr', 'bl', 'gr', 'st', 'sl', 'cl',
        'pl', 'fl', 'sm', 'sn', 'sp', 'sw'
        ]
    sentence = input('Enter a sentence: ')
    sentence = sentence.split()
    for P in range(len(sentence)):
        i = sentence[P]
        if len(i) == 1:
            sentence[P] = i + 'ay'
        elif i[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[P] = i+'ay'
        elif t(i) in lst:
            sentence[P] = i[2:]+i[:2]+'ay'
        elif i.isalpha() == False:
            sentence[P] = i
        else:
            sentence[P] = i[1:]+i[0]+'ay'
    return ' '.join(sentence)

def t(str):
    return str[0]+str[1]

if __name__ == "__main__":
    x = main()
    print(x)
