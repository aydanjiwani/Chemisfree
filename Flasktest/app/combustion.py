from parse import parse
import re
def combust(formula2):
    formula = parse(formula2)
    for i in formula:
        if(ord(i) == 67):
            carbons = float(formula[i])
        elif(ord(i) == 79):
            oxygens = float(formula[i])
        elif(ord(i) == 72):
            hydrogens = float(formula[i])
        else:
            print(i)
            print("Organic compounds only")
            return("Organic compounds only")
    co2 = carbons
    h2o = hydrogens/2
    flag = False
    oxygenneeded = 2*co2+h2o-oxygens
    print(carbons,hydrogens,oxygens)
    if(oxygenneeded < 0):
        oxygenneeded = oxygenneeded*-1
        flag = True
    if(flag):
        print(formula2 + " --> " + str(co2) + "co2 + " + str(h2o) + "h2o + " + str(oxygenneeded/2) + "o2")
        return(formula2 + " --> " + str(co2) + "co2" + str(h2o) + "h2o" + str(oxygenneeded/2) + "o2")
    else:
        print(formula2 + " + " +str(oxygenneeded/2) + " o2" + " --> " + str(co2) + "co2 + " + str(h2o) + "h2o")
        return(formula2 + " + " +  str(oxygenneeded/2) + " o2" + " --> " + str(co2) + "co2 + " + str(h2o) + "h2o")
combust("C6H12O6")

