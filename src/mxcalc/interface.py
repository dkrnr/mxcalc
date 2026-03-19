from mxcalc import calculate as calc

def getRowsAndColumns(num):
    """
    This is a fucntion to get rows and columns from user

    Args:
        num: identity number of the matrix
    Returns:
        values:both values as a list or -1 if error
    """

    try:
        row = int(input(f"Enter rows count of matrix {num} (eg :row x column):"))
        column = int(input(f"Enter column count of matrix {num} (eg :row x column):"))

        if(not (row>0 and column>0)):
            raise ValueError
        else:
            return [row,column]
    except ValueError:
        print("\nEnter a correct integer number above 0")
        
    return -1

def getMatrix(rows,columns):
    """
    This is a function to get matrix values according to the rows anc columns count

    Args:
        rows: the row count of the matrix
        columns: the column count of the matrix
    
    Returns:
        matrix: the matrix with all of the values
    """
    matrix = []
    print()
    for j in range(rows):
        matrix.append([])
        for k in range(columns):
            try:
                value =  int(input(f"Enter values for row {j+1}, column {k+1}:"))
                matrix[j].append(value)
            except ValueError as e:
                print("Error:","Enter a correct Integer value")
                return -1
    return matrix

def displayMatrix(matrix,isFinal=False):
    """
    This is a function to display the given matrix

    Args:
        matrices: matrix to be operated on as a list
        isFinal: if needs to be displayed as the final matrix
    """
    print()
    if (isFinal):
        print("The Final Matrix")
        print("=================")
    for l in range (len(matrix)):
        print(matrix[l])

def matrixMultiplicationHelper(matrices,i):
    """
    This is a function that provides user with an interface to perform matrix addition

    Args:
        matrices: main list to store all matrices
        i: number to record repeatitions
    """
    i = 1
    while i>0:
        print(f"\nEnter details for Matrix {i}")
        print("=====================")

        values = getRowsAndColumns(i)
        if(values == -1):
            continue

        matrix = getMatrix(values[0],values[1])
        if(matrix==-1):
                continue
        
        matrices.append(matrix)
        displayMatrix(matrix,False)
        i+=1
        if(i>2):
            break
        if(i>2 and input("\nAdd another Matrix to calculation (y if yes):").lower() != "y"):
            break  

    finalMatrix =  calc.matrixMultiplication(matrices)
    displayMatrix(finalMatrix,True)

def matrixAddSubHelper(matrices,oprt,i):
    """
    This is a function that provides user with an interface to perform matrix addition

    Args:
        matrices: main list to store all matrices
        oprt: the operator being used for calculation
        i: number to record repeatitions
    """
    values = getRowsAndColumns(i)
    if(values != -1):
        while i>0:
            print(f"\nEnter details for Matrix {i}")
            print("=====================")

            matrix = getMatrix(values[0],values[1])
            if(matrix==-1):
                continue

            matrices.append(matrix)
            displayMatrix(matrix,False)
            i+=1
            if(i>2 and input("\nAdd another Matrix to calculation (y if yes):").lower() != "y"):
                break

        finalMatrix = calc.matrixAddSub(matrices,oprt)
        displayMatrix(finalMatrix,True)
