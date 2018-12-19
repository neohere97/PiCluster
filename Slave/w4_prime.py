import rpyc
class MyService(rpyc.Service):
    def on_connect(self, conn):
        
        pass

    def on_disconnect(self, conn):
        
        pass

    def exposed_no_of_prime_numbers(self,upper,lower):   
        a = []      
        for num in range(lower,upper+1):       
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        break
                else:
                    a.append(num)       
        return a    
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18864)
    t.start()
