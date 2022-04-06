from time import perf_counter
import multiprocessing as mp
def logFile(time1,time2):
    f=open("merge.log","a")
    data = str(time1-time2)
    f.write("Elapsed time: "+ data)
    f.close()
def startTime():
    start= perf_counter()
    return start
def endTime():
    end = perf_counter()
    return end 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 #finding middle of array
        L = arr[:mid]

        R = arr[mid:]
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
def printList(arr):
    for i in range(len(arr)):
         print(arr[i], end=" ")
    
    print()
def dataInput():
    print("Input data file", end="\n")
#def logFile():
if __name__ == '__main__':
    arr = [12,11,13,5,6,7]
    print("Given array is", end="\n")
    printList(arr)
    proccess = mp.cpu_count()
    p = mp.Pool(processes=process)
    start = startTime()
    p.map(mergeSort(arr), range(1))
    p.close()
    end = endTime()
    print("Sort finished in: ",end-start)
    print("Sorted array is: ", end="\n")
    printList(arr)
    logFile(end,start)
