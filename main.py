import time
import random

#RADIX SORT
with open("teste.txt", 'r') as f:
    nr = int(f.readline())
    Laux = []
    for i in range(nr):
        Laux.append(f.readline().split(sep = ' '))
    for i in range(len(Laux)):
        Laux[i][0] = int(Laux[i][0])
        Laux[i][1].replace("\n",'')
        Laux[i][1] = int(Laux[i][1])

    print(Laux)
print("Puteti alege din urmatoarele teste: ")
for i in range(len(Laux)):
    print(f"{i}. pentru {Laux[i][0]} elemente si numere in intervalul [0,{Laux[i][1]}]")
test = int(input("Ce test doriti sa rulam? "))
L=[]
for i in range(int(Laux[test][0])):
    x= random.randint(0, int(Laux[test][1]))
    L.append(x)
L1 = L.copy()
L2 = L.copy()
L3 = L.copy()
L4 = L.copy()
L5 = L.copy()
L6 = L.copy()
L7 = L.copy()
L8 = L.copy()
L9 = L.copy()
# baza = int(input("Dati baza in care vom lucra: "))
timp1 = time.time()
def radix_sort(V):
    buckets = [[] for _ in range(10)]
    ok = 1
    radix = 1
    while ok == 1:
        ok = 0
        for i in V:
            buckets[(i//radix) % 10].append(i)
            if i//radix > 9:
                ok = 1
        radix *= 10
        V.clear()
        for i in range(10):
            for j in buckets[i]:
                V.append(j)
            buckets[i].clear()
radix_sort(L)
timp2 = time.time()
# print(timp2-timp1)
def test_radix(X):
    aux = sorted(X)
    radix_sort(X)
    if X == aux:
        return "DA"
    else:
        return "NU"
def test_merge(X):
    aux = sorted(X)
    merge_sort(X)
    if aux == X:
        return "DA"
    else:
        return "NU"
def test_shell(X):
    aux = sorted(X)
    shell_sort(X)
    if aux == X:
        return "DA"
    else:
        return "NU"
def test_tim(X):
    aux = sorted(X)
    timSort(X)
    if aux == X:
        return "DA"
    else:
        return "NU"


Timpi={}
Timpi["Radix_sort"] = [timp2-timp1, test_radix(L1)]
# print(Timpi)


#MERGE SORT
timp3 = time.time()

def merge_sort(V):
    if len(V) > 1:
        mij = len(V) // 2
        st = V[:mij]
        dr = V[mij:]
        merge_sort(st)
        merge_sort(dr)

        i=0
        j=0
        k=0

        while i < len(st) and j < len(dr):
            if st[i] <= dr[j]:
                V[k] = st[i]
                i+=1
            else:
                V[k] = dr[j]
                j+=1
            k+=1

        while i < len(st):
            V[k] = st[i]
            i += 1
            k += 1

        while j < len(dr):
            V[k] = dr[j]
            j += 1
            k += 1



merge_sort(L2)
timp4 = time.time()
Timpi["Merge_sort"] = [timp4 - timp3, test_merge(L3)]

#SHELL SORT
timp5 = time.time()
def shell_sort(V):
    size = len(V)
    gap = size // 2

    while gap > 0:
        for i in range (gap,size):
            ancora = V[i]
            j = i

            while j>= gap and V[j-gap] > ancora:
                V[j] = V[j-gap]
                j-=gap
            V[j] = ancora
        gap = gap//2
shell_sort(L4)
timp6 = time.time()
Timpi["Shell_sort"] = [timp6 - timp5, test_shell(L5)]

#TIM SORT
timp7 = time.time()
MIN_MERGE = 32


def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertionSort(arr, st, dr):
    for i in range(st + 1, dr + 1):
        j = i
        while j > st and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1



def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    st, dr = [], []
    for i in range(0, len1):
        st.append(arr[l + i])
    for i in range(0, len2):
        dr.append(arr[m + 1 + i])

    i, j, k = 0, 0, l


    while i < len1 and j < len2:
        if st[i] <= dr[j]:
            arr[k] = st[i]
            i += 1

        else:
            arr[k] = dr[j]
            j += 1

        k += 1


    while i < len1:
        arr[k] = st[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = dr[j]
        k += 1
        j += 1


def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)


    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)


    size = minRun
    while size < n:


        for st in range(0, n, 2 * size):


            mid = min(n - 1, st + size - 1)
            dr = min((st + 2 * size - 1), (n - 1))

            if mid < dr:
                merge(arr, st, mid, dr)

        size = 2 * size
timSort(L6)
timp8 = time.time()
Timpi["Tim_sort"] = [timp8 - timp7, test_tim(L7)]

# INTRO SORT

import math
from heapq import heappush, heappop

arr = []

def heapsort():
    global arr
    h = []


    for value in arr:
        heappush(h, value)
    arr = []


    arr = arr + [heappop(h) for i in range(len(h))]


def InsertionSort(start, end):
    st = start
    dr = end


    for i in range(st + 1, dr + 1):
        key = arr[i]


        j = i - 1
        while j >= st and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


def Partition(low, high):
    global arr

    pivot = arr[high]


    i = low - 1

    for j in range(low, high):


        if arr[j] <= pivot:


            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def MedianaDin3(a, b, d):
    global arr
    A = arr[a]
    B = arr[b]
    C = arr[d]

    if A <= B and B <= C:
        return b
    if C <= B and B <= A:
        return b
    if B <= A and A <= C:
        return a
    if C <= A and A <= B:
        return a
    if B <= C and C <= A:
        return d
    if A <= C and C <= B:
        return d



def IntrosortUtil(start, end, depthLimit):
    global arr
    size = end - start
    if size < 16:


        InsertionSort(start, end)
        return

    if depthLimit == 0:

        heapsort()
        return

    pivot = MedianaDin3(start, start + size // 2, end)
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])


    partitionPoint = Partition(start, end)



    IntrosortUtil(start, partitionPoint - 1, depthLimit - 1)
    IntrosortUtil(partitionPoint + 1, end, depthLimit - 1)



def Introsort(start, end):

    depthLimit = 2 * math.floor(math.log2(end - start))
    IntrosortUtil(start, end, depthLimit)



def main():
    global arr
    arr = arr + L8

    n = len(arr)

    timp9 = time.time()
    Introsort(0, n - 1)
    timp10 = time.time()

    aux = sorted(L8)
    if aux == arr:
        Timpi["Intro_sort"] = [timp10 - timp9, "DA"]
    else:
        Timpi["Intro_sort"] = [timp10 - timp9, "NU"]




if __name__ == '__main__':
    main()

def sortare_sort(X):
    timp9 = time.time()
    X=sorted(X)
    timp10 = time.time()
    return timp10 - timp9

Timpi["Python_sort"] = [sortare_sort(L9) ,"DA"]
print(Timpi)













