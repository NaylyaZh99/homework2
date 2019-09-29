import itertools

def combination(phone, number):
    combi = []
    for i in number:
        if i == '1':
            continue
        combi.append(phone[i])
    return [''.join(combo) for combo in itertools.product(*combi)]

ph = {'0': ' ', 
      '1': '', 
      '2': 'abc', 
      '3': 'def', 
      '4': 'ghi', 
      '5': 'jkl', 
      '6': 'mno', 
      '7': 'pqrs', 
      '8': 'tuv', 
      '9': 'wxyz'}
num = input()
print(combination(phone, num))

