import rpyc
import hashlib
class MyService(rpyc.Service):
    def on_connect(self, conn):
        
        pass

    def on_disconnect(self, conn):
        
        pass

    def exposed_no_of_prime_numbers(self,upper,lower):   
        a = []      
        for num in range(lower,upper+1):       
            if num > 1:
                for i in range(2,int(num/2)):
                    if (num % i) == 0:
                        break
                else:
                    a.append(num)       
        return str(len(a))    

    def exposed_decrypt(self,crypt_msg,upper,lower):
        for j in range(lower,upper):
            dec_msg = []
            orig_hash = crypt_msg[len(crypt_msg)-1]
            k = str(j)
            for l in range(len(crypt_msg)-1):
                dec_msg.append(chr(ord(crypt_msg[l]) - int((k[l % len(k)]))))
            dec_hash_msg = ''.join(dec_msg).encode()
            dec_hash = hashlib.sha1(dec_hash_msg).hexdigest()
            if dec_hash == orig_hash:
                return True, j
        return False,0

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18864)
    t.start()