def remove_character(get_cipher):
    size_cipher = len(get_cipher)
    cipher = ""
    for i in range(size_cipher):
        if 'a' <= get_cipher[i] <= 'z':
            cipher += get_cipher[i]
    return cipher


def size_key(cipher):
    size_cipher = 0
    size_frequency = 0
    s = 0
    range_list = []
    trigram = [0, 0, 0]
    frequency = [0] * 19

    cipher = remove_character(cipher)
    size_cipher = len(cipher)

    for i in range(size_cipher - 3):
        trigram[0] = cipher[i]
        trigram[1] = cipher[i+1]
        trigram[2] = cipher[i+2]
        for k in range(i + 1, size_cipher - 2):
            if trigram[0] == cipher[k] and trigram[1] == cipher[k+1] and trigram[2] == cipher[k+2]:
                if (k-i) not in range_list:
                    range_list.append(k-i)
                break
    size_frequency = len(range_list)
    for i in range(size_frequency):
        for k in range(2, 21):
            if range_list[i] % k == 0:
                frequency[k-2] += 1

    print("\n\n\nAnalisar possíveis tamanhos de chave por frequência e escolher um possível tamanho de chave:\n")
    for i in range(10):
        print("Possível tamanho de chave: {} = {}".format(i+2, frequency[i]))
    print("\nInsira o tamanho da chave: ")
    s = int(input())

    return s

def attack(cipher, sizeKey, language):
    sizeCipher = 0
    y = 0
    key = ""
    
    english = {'a':8.167,'b':1.492,'c':2.782,'d':4.253,'e':12.702,'f':2.228,
    'g':2.015,'h':6.094,'i':6.966,'j':0.153,'k':0.772,'l':4.025,'m':2.406,'n':6.749,'o':7.507,
    'p':1.929,'q':0.095,'r':5.987,'s':6.327,'t':9.056,'u':2.758,'v':0.978,'w':2.36,'x':0.15,
    'y':1.974,'z':0.074}

    portuguese = {'a':14.63,'b':1.04,'c':3.88,'d':4.99,'e':12.57,'f':1.02,
    'g':1.30,'h':1.28,'i':6.18,'j':0.4,'k':0.02,'l':2.78,'m':4.74,'n':5.05,'o':10.73,
    'p':2.52,'q':1.20,'r':6.53,'s':7.81,'t':4.34,'u':4.63,'v':1.67,'w':0.01,'x':0.21,
    'y':0.01,'z':0.47}

    frequencyCipher = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,
    'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,
    'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,
    'y':0,'z':0}

    cipher = remove_character(cipher)
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
