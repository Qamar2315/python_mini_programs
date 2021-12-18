#program to check whether a graph is having an eular circuit or an eular path
def isEulerCircuit(num):
    isEulerCircuit=True
    for i in num:
        if not isEven(i):
            isEulerCircuit=False
            break
    return isEulerCircuit
def isEulerPath(num):
    isEulerPath=False
    countOdd=0
    for i in num:
        if not isEven(i):
            countOdd+=1
    if countOdd<=2:
        isEulerPath=True
    return isEulerPath

def isEven(num):
    if num%2==0:
        return True
    else:
        return False
def main():
    vertics=eval(input("Enter the number of vertices"))
    degrees=[]
    for i in range(vertics):
        degree=eval(input(f"Enter degree of {i+1} vertex : "))
        degrees.append(degree)
    if (isEulerCircuit(degrees) and isEulerPath(degrees)):
        print("GIVEN GRAPH HAS BOTH EULAR CIRCUIT AND AS WELL AS EULAR PATH")
    elif(isEulerCircuit(degrees)):
        print("GIVEN GRAPH HAS ONLY EULAR CIRCUIT BUT NOT EULAR PATH")
    elif(isEulerPath(degrees)):
        print("GIVEN GRAPH HAS ONLY EULAR PATH BUT NOT EULAR CIRCUIT")
    else:
        print("GIVEN PATH HAS NEITHER EULAR CIRUIT NOR EULAR PATH")
main()
