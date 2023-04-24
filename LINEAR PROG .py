import pulp

#variables
problem = pulp.LpProblem("example_1", pulp.LpMinimize)
x= pulp.LpVariable("x", lowBound=0)
y= pulp.LpVariable("y", lowBound=0)

#objective function
problem += 3*x + 5*y

#constraints
problem += 2*x + 3*y >= 12
problem += -x + y <= 3
problem += x >= 4
problem += y <= 3

status = problem.solve()
print("problem\n", problem)
print("status", pulp.LpStatus[status])
print("Final Solution", pulp.value(x), pulp.value(y), pulp.value(problem.objective))
