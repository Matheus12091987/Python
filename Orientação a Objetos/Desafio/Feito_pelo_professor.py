def pare(a):
    hsh=[0 for _ in range(max(a)+1)]
    for i in a:
        if hsh[i]==1:
            return i
        else:
            hsh[i]=1

    return -1



a = [1,2,3,2,5,4]

print(pare(a))

