from z3 import *

i0 ,i1 ,i2 ,i3 = Bools('i0 i1 i2 i3')
w1,w2,w3 = Bools('w1 w2 w3')
	
out = Bools('out')

w1 = (Xor((Xor((Xor((i0),(i1),)),(i2),)),(i3),))
w2 = (And((i0),Not(i1),))
w3 = (Or((w2),Not(i1),))
out = Not(Xor((w1),(w3),))
	
