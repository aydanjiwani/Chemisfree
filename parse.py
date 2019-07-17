import re

def parse(formula)
    elements = []
    realelements = []
    r = re.compile("([a-zA-Z]+)([0-9]+)")
    formula = re.findall('[A-Z][^A-Z]*', formula)

    for i in range (0,len(formula)):
        elements.append(re.findall('[0-9]*[^0-9]*', formula[i]))
    for i in range (0,len(formula)):
        formula[i] = re.sub(r"\d+", "", formula[i])

    for i in range (0,len(elements)):
        if(elements[i][1] == ""):
            realelements.append(1)
        else:
            realelements.append(elements[i][1])
        
    compound = {}
    for i in range(0,len(formula)):
        compound[formula[i]]=realelements[i]
    return(compound)

