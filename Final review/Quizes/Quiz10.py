class University:
    def __init__(self, nm, lo, pr):
        self.nm = nm
        self.lo = lo
        self.pr = pr

    def __call__(self, cn, dean):
        return College(self.nm, self.lo, cn, dean)

class College:
    Purpose = "Professional Education"
    def __init__(self, un, lo, cn, dean):
        self.un = un
        self.lo = lo
        self.cn = cn
        self.dean = dean

um = University("U. of Michigan", "Ann Arbor", "John Cruz")
um.Purpose = "Research"
ocu = University("U. of North Texas", "Edmond", "Bob Betz")
ocucoa = ocu("College of Arts", "Christie")
ocucoa.lo = "Austin"

print(um.nm) # -> U. of Michigan
# print(ocu.Purpose) -> error, purpose is not defined for ocu so when it is called it will give an error
# purpose is defined for the class college not the class university
print(ocucoa.lo) # -> Austin
print(um.Purpose) # -> Research
print(ocucoa.Purpose) # -> Professional Education


for x in range(3):
    x = x+5
    print(x)
print(x)
for x in range(4):
    print(x)

# What is the 1st number that is printed: 5
# What is the 2nd number that is printed: 6
# What is the 3rd number that is printed: 7
# What is the 4th number that is printed: 7
# What is the 5th number that is printed: 0  








