""" cont = 0
for i in range(1,101):
    if i % 2 == 0:
        print(i)
        cont = cont + 1
    if cont == 20:
        break """

for i in range(1,101):
    if i % 2 == 0:
        continue
    else:
        print(i)