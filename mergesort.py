from time import perf_counter
import random
import multiprocessing as mp

# Used to write to a file named merge.log
def logFile(seqtime1,seqtime2,paratime1,paratime2): #Used to write to a file named merge.log
    f=open("merge.log","a")
    f.write("Sequential: \n")
    f.write("Elapsed time: ")
    f.write('{:.20f}'.format(seqtime1-seqtime2)+ "\n")
    f.write("Parallel: "+ "\n"+ "Elapsed time: ")
    f.write('{:.20f}'.format(paratime1-paratime2) +"\n")
    f.write("The Speed up of the program was: ")
    speedup = (seqtime1-seqtime2) // (paratime1-paratime2)
    f.write('{:.10f}'.format(speedup))
    f.close()


# Start Timer
def startTime():
    start= perf_counter()
    return start

# End Timer
def endTime():
    end = perf_counter()
    return end 

# Takes in an array and performs mergesort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2   # Finds middle of array
        L = arr[:mid]       # Splits left side of array

        R = arr[mid:]       # Splits right side
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Generates a number of element using a gaussian distribution
def generateNumbers(numElements):
    randomArray = []
    mu = 100
    sigma = 50

    for i in range(numElements):
        randomArray.append(int(random.gauss(mu, sigma)))
    return randomArray

def copyArray(arr):
    equalArray = []

    for i in range(len(arr)):
        equalArray.insert(i, arr[i])
    return equalArray


if __name__ == '__main__':
    # Generate & Display Data Array
    userIn = int(input("Enter the size of the array to be randomly generated ")) 
    arr1 = generateNumbers(userIn)
    arr2 = copyArray(arr1)
    print("Given array is: ", arr1[:5])

    # Do Sequential Merge Sort
    start = startTime()
    mergeSort(arr1)
    end = endTime()

    # Print Sequential Data
    print("Sorted Array is: ", arr1[:5])
    print("Sequential Merge Sort Finished in",'{:.20f}'.format(end-start), "\n")
    print("unsorted array: ", arr2[:5])

    # Do Parallel Merge Sort
    p = mp.Process(target=mergeSort(arr2))
    pStart = startTime()
    p.start()
    p.join()
    pEnd = endTime()

    # Print Parallel Data
    print("Sorted array is: ",arr2[:5]) 
    print("Sort finished in: ",'{:.20f}'.format(pEnd-pStart), end="\n")

    # Log data
    logFile(end,start,pEnd,pStart)

