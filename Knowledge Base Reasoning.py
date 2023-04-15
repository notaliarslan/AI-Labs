//Task 1
from kanren import *
a = var()
b = var()
a = run(1, a, eq(a, b), eq(b, 300))
print(a)

//Task 2
from kanren import *
parent = Relation()
facts(parent, ("Umer", "Usman"), ("Umer", "Ali"), ("Suleman", "Umer"), ("Nouman", "Suleman"))
a = var()
b= var()
q1 = run(1, a, parent(a, "Usman"))
q2 = run(2, a, parent("Umer", a))
q3 = run(1 , a,parent(a, b),parent(b, 'Usman'))
q4 = run(1 , a,parent(a, b),parent(b, 'Umer'))
print(q1)
print(q2)
