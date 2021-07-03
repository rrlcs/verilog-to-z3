from z3 import *

#Function to check validity of a formula

def valid(formula):

    s = Solver()

    s.add(Not(formula))

    if s.check() == unsat:

        print("Valid")

        return True

    else:

        # print s.model()

        print("Not Valid")

        return False

i0 ,i1 = Bools('i0 i1')
i2_2 = Bool('i2_2')
i2_1 = Bool('i2_1')
n4,n5 = Bools('n4 n5')

i2 = Bool('i2')
B = (And((n4 == And((i0),Not(i1),)), (n5 == And(Not(i0),(i1),)), (i2_2 == And(Not(n4),Not(n5),))))
formula = Implies(False, B)
valid(formula)