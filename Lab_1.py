

# Give a prefix representation of a proposition, of the form prop = ('OR', True, False)
# Write a function named evaluate, which will evaluate the proposition
def evaluate(formula):
    if (formula[0] == 'AND'):
        return AND(formula[1], formula[2])
    elif (formula[0] == 'OR'):
        return OR(formula[1], formula[2])
    elif (formula[0] == 'IF'):
        return IF(formula[1], formula[2])
    elif (formula[0] == 'IFF'):
        return IFF(formula[1], formula[2])
    elif (formula[0] == 'NOT'):
        return NOT(formula[1])
    
   

# Create a new version of your evaluate function, named evaluate_r, which also takes in a formula, but it is able to evaluate composite formulae, such as ('OR', ('NOT', True), ('AND', True, False))

def evaluate_r(formula):
    if (len(formula) < 3):
        conversion = list(formula)
        conversion.append(False)
        formula = tuple(conversion)
    if (type(formula[1]) is not bool):
        p = evaluate_r(formula[1])
    else:
        p = formula
    if (type(formula[2]) is not bool):
        q = evaluate_r(formula[2])
    else: 
        q = formula[2]

    return evaluate(((formula[0], p, q)))


