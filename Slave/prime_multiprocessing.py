import time
import multiprocessing
from math import ceil


def find_prime(ll, ul, array):
    k=0
    for num in range(ll, ul + 1):
        if num > 1:
            for i in range(2, int(ceil(num/2))):
                if (num % i) == 0:
                    break
            else:
                array[k] = num
                k+=1


if __name__=='__main__':
    start = 3
    num = 10000
    arr = []
    arr1 = multiprocessing.Array('i', ceil(num/5))
    arr2 = multiprocessing.Array('i', ceil(num/5))
    arr3 = multiprocessing.Array('i', ceil(num/5))

    p1 = multiprocessing.Process(target=find_prime, args=(start, int(num/3), arr1))
    p2 = multiprocessing.Process(target=find_prime, args=(int(num/3)+1, int(2*num/3), arr2))
    p3 = multiprocessing.Process(target=find_prime, args=(int(2*num/3)+1, num, arr3))

    t1 = time.time()
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    for i in range(len(arr1)):
        if arr1.__getitem__(i) != 0:
            arr.append(arr1.__getitem__(i))
    for i in range(len(arr2)):
        if arr2.__getitem__(i) != 0:
            arr.append(arr2.__getitem__(i))
    for i in range(len(arr3)):
        if arr3.__getitem__(i) != 0:
            arr.append(arr3.__getitem__(i))

    t2 = time.time()
    print("Time taken is - " + str(t2-t1))
    print(str(len(arr)-1))

