# mxcalc
this is package for matrix calculations, in this package there are mainly 2 modules,
1. `calculate` : contains the functions for calculations 
2. `interface` : contains helpers and other functions to i/o matrices

## available operations 
- addition (any amount of matrices)
- substraction (any amount of matrices)
- multiplication (2 matrices)

## requirements
-  Python >=3.10 

## how to use
1. install by using `pip install mxcalc`
2. if ur just using to get results rather than use the functions u can just use `mxcalc` module itself, an interface made using the functions will be at ur service
- when you run the module, it will first ask you for a operation, select the operation you wish to perform
- then you can provide the information the systems ask about the matrices, the you will get your result at the end
```bash
mxcalc 
```
3. if u want some of the helper functions (to display matrix,get matrix data), u can use the `interface` module, example show bellow
```python
from mxcalc import interface

interface.displayMatrix(
    [[1],
     [0]]
)
```
4. if u want to use the function to input matrices in code and get direct resulting output, u can use the `calculate` module. simple example given bellow.
```python
from mxcalc import calculate

calculate.matrixMultiplication([
    [[1,0]],
    [[1],
     [2]]
])
```
> All the available functions are mentioned down below in the master table

## `calculate`

|Function|Parameters|Description|Returns|
|---|---|---|---|
|matrixAddSub|matrices (list), oprt (str)|Adds or subtracts an array of matrices based on the operator provided (+ or -).|The resulting matrix (list of lists).|
|matrixMultiplication|matrices (list)|Multiplies two matrices after checking if their dimensions are compatible.|The product matrix, or -1 if dimensions are invalid.|

## `interface`

|Function|Parameters|Description|Returns|
|---|---|---|---|
|getRowsAndColumns|num (int)|Prompts user for matrix dimensions with input validation.|[rows, cols] or -1 on error.
|getMatrix|rows (int), columns (int)|Collects individual integer values from the user for a specific matrix size.|A 2D list (matrix) or -1.|
|displayMatrix|matrix (list), isFinal (bool)|Prints a matrix to the console, optionally adding a "Final Matrix" header.|None|
|matrixMultiplicationHelper|matrices (list), i (int)|Manages the UI flow for collecting and multiplying two matrices.|None (displays result).|
|matrixAddSubHelper|matrices (list), oprt (str), i (int)|Manages the UI flow for adding/subtracting multiple matrices of the same size.|None (displays result).|

## improvements to make

### [ X ] make this a package
currently you can only use this by running `main.py` and using the helper interfaces provided by that, i feel like making it a package would give it a much better range
(inspired by githubs workflow suggestions)

### [ ... ] Add more operation
this operations are wayy too common. for example i want to add,
1. transpose
2. invertion(obviously)
3. rotation
and maybe flipping ? idk, we'll see

### [ ... ] multiple matrix calculations
right now only additions and substraction has unlimited amount of matrices support, idk if this is even possible but if we can do this it'll be fun