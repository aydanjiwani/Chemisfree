import json
from parse import parse
with open('chemdata.json') as json_file:  
    data = json.load(json_file)


print(data[0]['atomicMass'][:-3])
print(len(data))

def molarMass(formula2):
    masses = []
    totalmass = 0
    placeholder = -1
    formula = parse(formula2)
    for i in formula:
        for j in range(0,len(data)):
            if(i == data[j]['symbol']):
                masses.append(float(data[j]['atomicMass'][:-3]))
                continue
    print(masses)
    for i in formula.values():
        placeholder+=1
        totalmass += float(i)*masses[placeholder]
    print(totalmass)
    return(totalmass)


                

