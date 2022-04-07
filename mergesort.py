from time import perf_counter
import random
import multiprocessing as mp

# Used to write to a file named merge.log
def logFile(seqtime1,seqtime2,paratime1,paratime2, speedup): #Used to write to a file named merge.log
    f=open("merge.log","a")
    f.write("Sequential: \n")
    f.write("Elapsed time: ")
    f.write('{:.20f}'.format(seqtime1-seqtime2)+ "\n")
    f.write("Parallel: "+ "\n"+ "Elapsed time: ")
    f.write('{:.20f}'.format(paratime1-paratime2) +"\n")
    f.write("The Speed up of the program was: ")
    f.write('{:.10f}'.format(speedup) +"\n")
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

def sumArray(arr):
    sum = 0

    for i in arr:
        sum += i
    return sum

if __name__ == '__main__':
    # Generate & Display Data Array
    userInArraySize = int(input("Enter the size of the array to be randomly generated: "))
    userInRunTimes = int(input("Enter the number of times you would like to run with random data: "))

    # Run and store times 10 times to get average times
    sTimeArr = []
    pTimeArr = []
    avgSTime = []
    avgPTime = []
    for x in range(userInRunTimes):
        arr1 = generateNumbers(userInArraySize)
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
        sTimeArr.append(end-start)

        # Do Parallel Merge Sort
        p = mp.Process(target=mergeSort(arr2))
        pStart = startTime()
        p.start()
        p.join()
        pEnd = endTime()

        # Print Parallel Data
        print("Sorted array is: ",arr2[:5])
        print("Sort finished in: ",'{:.20f}'.format(pEnd-pStart), end="\n")
        pTimeArr.append(pEnd-pStart)

        # Print Speedup
        speedup = (end - start) // (pEnd - pStart)

        # Log data
        #logFile(end,start,pEnd,pStart)
        logFile(end,start,pEnd,pStart,speedup)

    sAvg = sumArray(sTimeArr) / len(sTimeArr)
    print("Average Sequential Sort: ", sAvg, end="\n")
    pAvg = sumArray(pTimeArr) / len(pTimeArr)
    print("Average Parallel Sort: ", pAvg, end="\n")
    avgSpeedup = sAvg // pAvg
    print("Average Speedup: ", avgSpeedup, end="\n")
