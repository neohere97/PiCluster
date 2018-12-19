import rpyc
import multiprocessing
from math import ceil
class MyService(rpyc.Service):
    def on_connect(self, conn):
        
        pass

    def on_disconnect(self, conn):
        
        pass

    def exposed_no_of_prime_numbers_parallel(self,start,num):   
        arr = []
        arr1 = multiprocessing.Array('i', ceil(num/5))
        arr2 = multiprocessing.Array('i', ceil(num/5))
        arr3 = multiprocessing.Array('i', ceil(num/5))
        arr4 = multiprocessing.Array('i', ceil(num / 5))

        p1 = multiprocessing.Process(target=self.find_prime, args=(start, int(num/4), arr1))
        p2 = multiprocessing.Process(target=self.find_prime, args=(int(num/4)+1, int(num/2), arr2))
        p3 = multiprocessing.Process(target=self.find_prime, args=(int(num/2)+1, int((3*num/4)+1), arr3))
        p4 = multiprocessing.Process(target=self.find_prime, args=(int((3*num/4)+1) + 1, num, arr4))
        p1.start()
        p2.start()
        p3.start()
        p4.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()

        for i in range(len(arr1)):
            if arr1.__getitem__(i) != 0:
                arr.append(arr1.__getitem__(i))
        for i in range(len(arr2)):
            if arr2.__getitem__(i) != 0:
                arr.append(arr2.__getitem__(i))
        for i in range(len(arr3)):
            if arr3.__getitem__(i) != 0:
                arr.append(arr3.__getitem__(i))
        for i in range(len(arr4)):
            if arr4.__getitem__(i) != 0:
                arr.append(arr4.__getitem__(i))
         
        return arr    

    def find_prime(self,ll, ul, array):
        k=0
        for num in range(ll, ul + 1):
            if num > 1:
                for i in range(2, int(ceil(num/2))):
                    if (num % i) == 0:
                        break
                else:
                    array[k] = num
                    k+=1


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()