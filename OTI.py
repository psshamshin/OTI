alphabet = []
dict = {}
gap = []
type_ = int(input("code/decode (1/2): "))
code = input("input: ")
if type_ == 1:
    for i in range(len(code)):
        if not code[i] in alphabet:
            alphabet.append(code[i])
    gen = int(input("ranges table custom/generated (1/2): "))
    if gen == 1:
        for i in range(len(alphabet)):
            limit = list(map(float, input(('gap ' + alphabet[i] + ' = ')).split('-')))
            limit.append(round(limit[1] - limit[0], 10))
            # print(range)
            dict[(alphabet[i])] = limit
            # print(dict[(alphabet[i])])
    elif gen == 2:
        print('alphabet:')
        s = 0.0
        for i in range(len(alphabet)):
            posibility = code.count(alphabet[i]) / len(code)
            dict[(alphabet[i])] = [s, round(s + posibility, 10), posibility]
            print(alphabet[i], dict[(alphabet[i])])
            s = round(s + posibility, 10)
    print('________')
    temp = [dict[(code[0])][0], dict[(code[0])][1]]
    print(code[0], "|", *temp)
    for i in range(1, len(code)):
        prev_temp = temp[0]
        delta = round(temp[1] - temp[0], 10)
        temp[0] += (delta * dict[(code[i])][0])
        temp[1] = round(prev_temp + (delta * dict[(code[i])][1]), 10)
        print(code[i], "|", *temp)
elif type_ == 2:
    alphabet = input('alphabet: ')
    for i in range(len(alphabet)):
        limit = list(map(float, input(('gap ' + alphabet[i] + ' = ')).split('-')))
        limit.append(round(limit[1] - limit[0], 10))
        # print(range)
        dict[(alphabet[i])] = limit
        # print(dict[(alphabet[i])])
    code = float(code)
    answer = []
    flag = True
    count = 0
    while flag and (count < 10):
        count += 1
        for i in range(len(alphabet)):
            if dict[(alphabet[i])][1] > code >= dict[(alphabet[i])][0]:
                print(alphabet[i], ' | ', code)
                answer.append(alphabet[i])
                code = round((code - dict[(alphabet[i])][0]) / (dict[(alphabet[i])][1] - dict[(alphabet[i])][0]), 10)
                # print(alphabet[i], answer.count(alphabet[i]) / len(answer), dict[(alphabet[i])][2])
                # if len(answer) > 1: # print(answer[-1], answer[-2])
                if (answer.count(alphabet[i]) / len(answer)) == dict[(alphabet[i])][2] and code == 0:
                    # dict[(answer[-1])][1] >= code >= dict[(answer[-1])][0]:
                    flag = False
                    break
    print(*answer)
