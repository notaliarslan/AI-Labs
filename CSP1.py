from constraint import *

CSP= Problem()

CSP.addVariable("Sat 3:30pm", ["Up","Captain America","When a Stranger Call", "Sully"])
CSP.addVariable("Sat 8:30pm", ["Up","Captain America","When a Stranger Call", "Sully"])
CSP.addVariable("Sun 3:30pm", ["Up","Captain America","When a Stranger Call", "Sully"])
CSP.addVariable("Sun 8:30pm", ["Up","Captain America","When a Stranger Call", "Sully"])


CSP.addConstraint(lambda t1,t2,t3,t4: t1!=t2 and t1!=t3 and t1!=t4,["Sat 3:30pm","Sat 8:30pm","Sun 3:30pm","Sun 8:30pm"])
CSP.addConstraint(lambda t1,t2,t3,t4: t2!=t1 and t2!=t3 and t2!=t4,["Sat 3:30pm","Sat 8:30pm","Sun 3:30pm","Sun 8:30pm"])
CSP.addConstraint(lambda t1,t2,t3,t4: t3!=t2 and t3!=t1 and t3!=t4,["Sat 3:30pm","Sat 8:30pm","Sun 3:30pm","Sun 8:30pm"])
CSP.addConstraint(lambda t1,t2,t3,t4: t4!=t3 and t4!=t2 and t4!=t1,["Sat 3:30pm","Sat 8:30pm","Sun 3:30pm","Sun 8:30pm"])

sol = CSP.getSolutions()
print(sol)
