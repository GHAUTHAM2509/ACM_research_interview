# Adding 3 numbers.

## Description:-

Finding the sum of 3 numbers using python and pennylane framework.

## Prerequisites
Pennylane module and python are required.
```
pip install pennylane
```

## Usage
In the terminal once u run the program enter 3 numbers in 3 different lines and the sum of the numbers will the diplayed in the 4th line.

## Working
**The program makes use of pennylane to create multiple devices and hence qubits to execute the code. <br>
The 3 major logic circuits in the program are the AND gate , OR gate & XOR gate.<br>
All the 3 gates take only 2 inputs and give out the logical output.**
<br><br><br>
**The major Function that handles the logic of the Program is the ***sumof2 function*** which is basically a full-adder logic circuit**

## Main Function. 
**This function takes the input converts it to binary form sends it to the full adder bit by bit and the stoes the sum value in a array and carryout value in carryin for the next iteration.
Now the array which contains the binary form of the sum of 2 numbers in reverse order is used to find the decimal value.(The array is reversed for easy calculation but it is reversed inside to verify if the program is working properly).Both the ***reverse()*** can be removed.**
```python
sum([(2**((i)*ar1[i])*ar1[i]) for i in range(len(ar1))])
```
**Now that the sum of 2 numbers is obtained the same is done with the third num and the sum of 2 numbers to get the sum of 3 numbers**

## Quantum Circuits

### OR Gate and AND Gate.
```plaintext

div1
-----------
|         |
| q[0]    |-----[ Probability Measurement ]
|         |
-----------
   |
   |  
-----------
|         |
| q[1]    |-----[ Ignored Measurement ]
|         |
-----------

div2
-----------
|         |
| q[0]    |-----[ Ignored Measurement ]
|         |
-----------
   |
   |  
-----------
|         |
| q[1]    |-----[ Probability Measurement ]
|         |
-----------

```
**The Measured values are the manipulated to get the desired result.**
### XOR Gate.
```plaintext
-----------
|         |
| q[0]    |-----[ CNOT ]-----
|         |                 |
-----------                 |
                            |
-----------                 |
|         |                 |
| q[1]    |------------------[ Probability Measurement ]
|         |
-----------

```
**The combination of the 3 gates gives the full adder.**
**SUM**
```plaintext

-----------
| NUM1     |-----[ CNOT ]-----
-----------                 |
                            |
-----------                 |
| NUM2     |-----------------------[ CNOT ]-----
-----------                                    |
                                               |
                                               |
                                     -----------
                                     | q[1]    |---[ SUM ]
                                     -----------

```
**Carry**
```plaintext
-----------
| NUm1    |-----[ CNOT ]-----                
-----------                 |
                            |
-----------                 |               
| NUM2    |-----------------------|---
-----------    -----------        | ---AND                   
               | carry   |--------|---
               -----------        |
                                  |---------┌───┐
                                            ┤ X ├--o─--┐
                                            └───┘  │   │
-----------                       -----------------o---┼--- OR       
| NUM1    |-----------------------|---                 |          -----------
-----------    -----------        | ---AND             |----------| carry   |   
               | NUM2    |--------|---                            ----------- 
               -----------

```

## TRUTH TABLE

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |   0  |
| 0 | 0 |  1  |  1  |   0  |
| 0 | 1 |  0  |  1  |   0  |
| 0 | 1 |  1  |  0  |   1  |
| 1 | 0 |  0  |  1  |   0  |
| 1 | 0 |  1  |  0  |   1  |
| 1 | 1 |  0  |  0  |   1  |
| 1 | 1 |  1  |  1  |   1  |

## Output
![image](https://github.com/GHAUTHAM2509/ACM_research_interview/assets/138212014/0f015624-c207-45d0-8f0f-d3d42c092b30)






               
                               


