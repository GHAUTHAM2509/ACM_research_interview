import pennylane as qml
from pennylane import numpy as np

#############################################  AND GATE 

devand1 = qml.device('default.qubit', wires=2)

@qml.qnode(devand1)
def circuitand1(x=None, y=None):
    qml.BasisState(np.array([x,y]), wires=[0,1])
    return (qml.probs(wires=[0]))

devand2 = qml.device('default.qubit', wires=2)

@qml.qnode(devand2)
def circuitand2(x=None, y=None):
    qml.BasisState(np.array([x,y]), wires=[0,1])
    return (qml.probs(wires=[1]))


def outputand(a,b):
    if circuitand1(x=a,y=b)[1] + circuitand2(x=a,y=b)[1] > 1:
        return 1
    else:
        return 0


############################################### OR GATE

dev1 = qml.device('default.qubit', wires=2)

@qml.qnode(dev1)
def circuitor1(x=None, y=None):
    qml.BasisState(np.array([x,y]), wires=[0,1])
    return (qml.probs(wires=[0]))

dev2 = qml.device('default.qubit', wires=2)

@qml.qnode(dev2)
def circuitor2(x=None, y=None):
    qml.BasisState(np.array([x,y]), wires=[0,1])
    return (qml.probs(wires=[1]))


def outputor(a,b):
    if circuitor1(x=a,y=b)[1] + circuitor2(x=a,y=b)[1] > 0:
        return 1
    else:
        return 0

################################################ XOR GATE

devxor = qml.device('default.qubit', wires=2)

@qml.qnode(devxor)
def circuitxor(x=None, y=None):
    qml.BasisState(np.array([x,y]), wires=[0,1])
    qml.CNOT(wires=[0,1])
    return qml.probs(wires=[1])


def outputxor(a,b):
    return (circuitxor(x=a,y=b)[1])
 


###############################################  BINARY CONVERSION

def Binary(a):
    return bin(a)[2:]

################################################ FULL ADDER


def sumof2(number1,number2,carryin):

    SUM = outputxor(outputxor(number1,number2),carryin)
    #print(SUM)

    carryOUT = outputor(outputand(number1,number2),outputand(outputxor(number1,number2),carryin))
    #print(carryOUT)

    return int(SUM),int(carryOUT)

####################################### PROGRAM TO FIND THE SUM OF 3 NUMBERS.


num_1 = int(input())
num_2 = int(input())
num_3 = int((input()))
def major_sum(num_1,num_2):
    num_1 = Binary(num_1) 
    num_2 = Binary(num_2)
    arr = []
    
    max_len = max(len(num_1), len(num_2))
    num_1 = num_1.zfill(max_len)
    num_2 = num_2.zfill(max_len)
    carryin = 0

    for i in range(max_len - 1, -1, -1):
        ele, carryin = sumof2(int(num_1[i]), int(num_2[i]), carryin)
        arr.append(ele)

    if carryin:
        arr.append(carryin)

    
    arr.reverse()
    return arr

ar1 = major_sum(num_1,num_2)
ar1.reverse()
new_num = sum([(2**((i)*ar1[i])*ar1[i]) for i in range(len(ar1))])


ar2 = major_sum(new_num,num_3)
ar2.reverse()
FINAL_num = sum([(2**((i)*ar2[i])*ar2[i]) for i in range(len(ar2))])
print(FINAL_num)



######################################################################################################################










