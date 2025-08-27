import numpy as np

def addition(arr1, arr2):
    result = arr1 + arr2
    print(f"Addition of the two matrices is: \n{result}")
    return result


def substraction(arr1, arr2):
    result = arr1 - arr2
    print(f"Substraction of the two matrices is: \n{result}")
    return result


def multiplication(arr1, arr2):
    result = arr1 @ arr2
    print(f"Multiplication of the two matrices is: \n{result}")
    return result


def transpose(array):
    result = array.T
    print(f"Transpose of the matrix is: \n{result}")
    return result


def inverse(array):
    result = np.linalg.inv(array)
    print(f"Inverse of the matrix is: \n{result}")
    return result


def determinant(array):
    result = np.linalg.det(array)
    print(f"Determinant of the matrix is: \n{result}")
    return result


def option(opt, arr1, arr2=None):
    try:
        match opt:
            case 1:
                return addition(arr1, arr2)
            case 2:
                return substraction(arr1, arr2)
            case 3:
                return multiplication(arr1, arr2)
            case 4:
                return transpose(arr1)
            case 5:
                return inverse(arr1)
            case 6:
                return determinant(arr1)
    except ValueError:
        print()
        print("ERROR! Please check the order of matrix!")
    except:
        print()
        print("Something went wrong. Try Again!!")


def matrix(name = "Matrix"):
    try:
        rows = int(input(f"Enter the number of rows of the {name}: "))
        cols = int(input(f"Enter the number of columns of the {name}: "))

        elements = list(map(int, input(f"Enter {rows*cols} element, each seperated by a space: ").split()))
        array = np.array(elements).reshape(rows, cols)

        print(f"Your {name} is: \n{array}")
        return array
    except ValueError:
        print()
        print("ERROR! Please check the order of matrix!")
        print()
        main()
    except:
        print()
        print("Something went wrong. Try Again!!")
        print()
        main()

def main():
    print("=====================================")
    print("Please Select an Operation to perform")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Inverse")
    print("6. Determinant")
    print("=====================================")

    print()
    opt = int(input("Please select an operation to perform: "))
    print()

    while True:
        if opt in [1, 2, 3]:
            arr1 = matrix("Matrix A")
            print()
            arr2 = matrix("Matrix B")
            print()
            option(opt, arr1, arr2)
            break
        elif opt in [4, 5, 6]:
            arr1 = matrix("Matrix")
            print()
            option(opt, arr1)
            break
        else:
            print("Invalid Option!")
            opt = int(input("Please select a valid operation to perform: "))


if __name__ == '__main__':
    main()


