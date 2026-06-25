# Combinadic operator

## The mapping
every possible combination for a particular n and k values are mapped to number ranging from 1 to nCk and the number 0 is used to represent no state(not vaccum state)

the ac(x,y,l) is annihilation and creation operator working on a state of fixed n and k 
and output the state with same n and k 
it has two function insdide them, a(x,l) and c(y,l) which are annihilation and creation operators which may result in states for different k values 

so we assume that these operators are used together, which is the case for all the non relativstic Hamiltonian 

thus when these two are operate together we are still in the same space of n and k 

ac(x,y,l): the argument x is the index of the creation operator and y is index of the annihilation operator and l being the list representing the state 

for example:
ac(4,2,[3,2,0]) this will return 1 and [4,3,0] where the first output is bit that represent the phase of the state after this operation if 1 then negative if 0 then positive
