all = {}
output = set()
while True:
    inp = input()
    if inp == 'КОНЕЦ':
        break
    inp = inp.split('; ')
    all[inp[1]] = inp[0]

win = input().split(' ')
for i in win:
    if i in all:
        output.add(all[i])

output = list(output)
output.sort()


out = ''
for i in output:
    out += i
    if output[-1] != i:
        out += ', '

print(out)
