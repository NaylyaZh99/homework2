counter = {}
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)
for i in lines:
    line = i.split(' ')
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
for word in counter:
    if counter[word] == max_count:
        print (word)

