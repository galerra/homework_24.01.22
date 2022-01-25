def calc(z):
    a = ('M','N','O')
    b = ('L','M','O')
    c = ('L','M','N')
    if len(z) == 3:
        if z[0] == z[-1]:
            return 0
        else:
            if z[0] in a and z[1] in b and z[2] in c:
                return 1
            else:
                return 0
    else:
        return 0
z = ('N','O','M')
print(calc(z))