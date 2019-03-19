

a = [1,5,6,5,7]
novalista = []
value=0

for item in a:
    if item in novalista:
        value=item
        break
    else:
        novalista.append(item)

if value == 0:
    value = -1

print("primeiroDuplicado(a) = {}".format(value))