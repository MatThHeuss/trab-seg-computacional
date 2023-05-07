import math

def removeCharacter(getCipher):
    sizeCipher = 0
    cipher = ""

    sizeCipher = len(getCipher)
    for i in range(sizeCipher):
        if 'a' <= getCipher[i] <= 'z':
            cipher += getCipher[i]

    return cipher


def sizeKey(cipher):
    size_cipher = 0
    size_frequency = 0
    s = 0
    _range = []
    trigram = [0, 0, 0]
    frequency = [0] * 19

    cipher = removeCharacter(cipher)
    size_cipher = len(cipher)

    for i in range(size_cipher - 3):
        trigram[0] = cipher[i]
        trigram[1] = cipher[i + 1]
        trigram[2] = cipher[i + 2]
        for k in range(i + 1, size_cipher - 2):
            if trigram[0] == cipher[k] and trigram[1] == cipher[k + 1] and trigram[2] == cipher[k + 2]:
                if (k - i) not in _range:
                    _range.append(k - i)
                break

    size_frequency = len(_range)
    for i in range(size_frequency):
        for k in range(2, 20):
            if _range[i] % k == 0:
                frequency[k - 2] += 1

    print("\nAnalyze possible key sizes by frequency and choose a possible key size:\n")
    for i in range(10):
        print("Possible key size: ", i + 2, " = ", frequency[i])
    s = int(input("\nEnter key size: "))

    return s



def attack(cipher, sizeKey, language):
    sizeCipher = 0
    y = 0
    key = ""
    english = {ord('a'): 8.167, ord('b'): 1.492, ord('c'): 2.782, ord('d'): 4.253, ord('e'): 12.702, 
            ord('f'): 2.228, ord('g'): 2.015, ord('h'): 6.094, ord('i'): 6.966, ord('j'): 0.153, 
            ord('k'): 0.772, ord('l'): 4.025, ord('m'): 2.406, ord('n'): 6.749, ord('o'): 7.507, 
            ord('p'): 1.929, ord('q'): 0.095, ord('r'): 5.987, ord('s'): 6.327, ord('t'): 9.056, 
            ord('u'): 2.758, ord('v'): 0.978, ord('w'): 2.36, ord('x'): 0.15, ord('y'): 1.974, 
            ord('z'): 0.074}

    portuguese = {ord('a'): 14.63, ord('b'): 1.04, ord('c'): 3.88, ord('d'): 4.99, ord('e'): 12.57, 
                ord('f'): 1.02, ord('g'): 1.30, ord('h'): 1.28, ord('i'): 6.18, ord('j'): 0.4, 
                ord('k'): 0.02, ord('l'): 2.78, ord('m'): 4.74, ord('n'): 5.05, ord('o'): 10.73, 
                ord('p'): 2.52, ord('q'): 1.20, ord('r'): 6.53, ord('s'): 7.81, ord('t'): 4.34, 
                ord('u'): 4.63, ord('v'): 1.67, ord('w'): 0.01, ord('x'): 0.21, ord('y'): 0.01, 
                ord('z'): 0.47}

    frequencyCipher = {ord('a'): 0, ord('b'): 0, ord('c'): 0, ord('d'): 0, ord('e'): 0, ord('f'): 0,
                    ord('g'): 0, ord('h'): 0, ord('i'): 0, ord('j'): 0, ord('k'): 0, ord('l'): 0, 
                    ord('m'): 0, ord('n'): 0, ord('o'): 0, ord('p'): 0, ord('q'): 0, ord('r'): 0, 
                    ord('s'): 0, ord('t'): 0, ord('u'): 0, ord('v'): 0, ord('w'): 0, ord('x'): 0, 
                    ord('y'): 0, ord('z'): 0}

    cipher = removeCharacter(cipher)
    sizeCipher = len(cipher)

    y = sizeCipher // sizeKey

    x = 100 / float(y)

    frequencyCipher = {i: 0 for i in range(97, 123)}

    for i in range(sizeKey):
        for j in range(97, 123):
            frequencyCipher[j] = 0

        for j in range(y):
            frequencyCipher[ord(cipher[(j*sizeKey)+i])] += x

        key += '0'
        min_diff = 999999
        for w in range(26):
            difference = 0
            ind = 0
            for z in range(ord('a'), ord('z')+1):
                if z + w > ord('z'):
                    ind = z + w - 26
                else:
                    ind = z + w
                if language == 1:
                    if english[z] > frequencyCipher[ind]:
                        difference += (english[z] - frequencyCipher[ind])
                    else:
                        difference += (frequencyCipher[ind] - english[z])
                else:
                    if portuguese[z] > frequencyCipher[ind]:
                        difference += (portuguese[z] - frequencyCipher[ind])
                    else:
                        difference += (frequencyCipher[ind] - portuguese[z])

            if difference < min_diff:
                min_diff = difference
                key = key[:-1] + chr(ord('a')+w)

    print("\nChave:", key)
    return key
