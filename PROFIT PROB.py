import pulp
problem = pulp.LpProblem("Profit_Problem", pulp.LpMaximize)

A= pulp.LpVariable("A", lowBound= 0, cat= "Integer")
B= pulp.LpVariable("B", lowBound= 0, cat= "Integer")

#objective functions

problem += 30000*A + 45000*B

#constraints

problem += 3*A + 4*B <= 30
problem += 5*A + 6*B <= 60
problem += 1.5*A + 3*B <= 21

status = problem.solve()
print("problem\n", problem)
print("Status", pulp.LpStatus[status])
print("Solution", pulp.value(A), pulp.value(B), pulp.value(problem.objective))