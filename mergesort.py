from time import perf_counter
import random
import multiprocessing as mp

def logFile(time1,time2): #Used to write to a file named merge.log
    f=open("merge.log","a")
    data = str(time1-time2)
    f.write("Elapsed time: "+ data + "\n")
    f.close()

def startTime():
    start= perf_counter()
    return start

def endTime():
    end = perf_counter()
    return end 

def mergeSort(arr): #takes in an array and performs mergesorts
    if len(arr) > 1:
        mid = len(arr)//2 #finding middle of array
        L = arr[:mid] #splits left side of array

        R = arr[mid:] #splits right side
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

# used for printing the array, just used for testing probably omit this function
def printList(arr):
    for i in range(len(arr)):
         print(arr[i], end=" ")
    
    print()

# Generates a number of element using a gaussian distribution
def generateNumbers(numElements):
    randomArray = []
    mu = 100
    sigma = 50

    for i in range(numElements):
        randomArray.append(random.gauss(mu, sigma))

    return randomArray

if __name__ == '__main__':
    arr = [12,11,13,5,6,7]
    arr = generateNumbers(10) # Generate 10 random numbers in a normal distribution
    print("Given array is", end="\n")
    printList(arr)
    start = startTime()
    mergeSort(arr)
    #p = mp.Process(target=mergeSort, args=arr)
    #p.start()
    #p.join()
    end = endTime()
    print("Sort finished in: ",end-start)
    print("Sorted array is: ", end="\n")
    printList(arr)
    logFile(end,start)
