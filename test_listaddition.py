class obj1:
    pimmel = 1
    peter = 2

class obj2:
    def pimmelplus1(pimmel):
        pimmel += 1

obj2.pimmelplus1(obj1.pimmel)

print(obj1.pimmel)
