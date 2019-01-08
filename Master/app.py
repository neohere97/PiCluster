import rpyc
import time
import httplib2
import requests
import threading
import json
import hashlib
from flask import Flask,request

app = Flask(__name__)



@app.route('/runPrimeFivePi', methods=['POST'])
def FivePrime():
    data = json.loads(request.data.decode("utf-8"))    
    range_splits = splitRange(data["Upper Limit"],data["Lower Limit"],20)    
    t= threading.Thread(target=PrimeFive,args=(range_splits,))
    t.start()
    return "OK"


@app.route('/runPrimeOnePi', methods=['POST'])
def OnePrime():
    data = json.loads(request.data.decode("utf-8"))    
    range_splits = splitRange(data["Upper Limit"],data["Lower Limit"],4)    
    t= threading.Thread(target=PrimeOne,args=(range_splits,))
    t.start()            
    return "OK"

@app.route('/runBruteFivePi', methods=['POST'])
def FiveBrute():
    data = json.loads(request.data.decode("utf-8"))    
    crypt_msg = encrypt(data['Message'],data['Password'])    
    t= threading.Thread(target=BruteFive,args=(crypt_msg,))
    t.start()
    return "OK"

@app.route('/runBruteOnePi', methods=['POST'])
def OneBrute():
    data = json.loads(request.data.decode("utf-8"))    
    crypt_msg = encrypt(data['Message'],data['Password'])    
    t= threading.Thread(target=BruteOne,args=(crypt_msg,))
    t.start()
    return "OK"
    

def PrimeFive(range_splits):    

    k1 = rpyc.connect('192.168.2.101',18861)
    l1 = rpyc.connect('192.168.2.102',18861)
    m1 = rpyc.connect('192.168.2.103',18861)
    n1 = rpyc.connect('192.168.2.104',18861)
    o1 = rpyc.connect('192.168.2.105',18861)

    k2 = rpyc.connect('192.168.2.101',18862)
    l2 = rpyc.connect('192.168.2.102',18862)
    m2 = rpyc.connect('192.168.2.103',18862)
    n2 = rpyc.connect('192.168.2.104',18862)
    o2 = rpyc.connect('192.168.2.105',18862)


    k3 = rpyc.connect('192.168.2.101',18863)
    l3 = rpyc.connect('192.168.2.102',18863)
    m3 = rpyc.connect('192.168.2.103',18863)
    n3 = rpyc.connect('192.168.2.104',18863)
    o3 = rpyc.connect('192.168.2.105',18863)


    k4 = rpyc.connect('192.168.2.101',18864)
    l4 = rpyc.connect('192.168.2.102',18864)
    m4 = rpyc.connect('192.168.2.103',18864)
    n4 = rpyc.connect('192.168.2.104',18864)
    o4 = rpyc.connect('192.168.2.105',18864)

    k11 = rpyc.async_(k1.root.no_of_prime_numbers)(range_splits[0][1],range_splits[0][0])
    k22 = rpyc.async_(k2.root.no_of_prime_numbers)(range_splits[1][1],range_splits[1][0]+1)
    k33 = rpyc.async_(k3.root.no_of_prime_numbers)(range_splits[2][1],range_splits[2][0]+1)
    k44 = rpyc.async_(k4.root.no_of_prime_numbers)(range_splits[3][1],range_splits[3][0]+1)

    l11 = rpyc.async_(l1.root.no_of_prime_numbers)(range_splits[4][1],range_splits[4][0]+1)
    l22 = rpyc.async_(l2.root.no_of_prime_numbers)(range_splits[5][1],range_splits[5][0]+1)
    l33 = rpyc.async_(l3.root.no_of_prime_numbers)(range_splits[6][1],range_splits[6][0]+1)
    l44 = rpyc.async_(l4.root.no_of_prime_numbers)(range_splits[7][1],range_splits[7][0]+1)

    m11 = rpyc.async_(m1.root.no_of_prime_numbers)(range_splits[8][1],range_splits[8][0]+1)
    m22 = rpyc.async_(m2.root.no_of_prime_numbers)(range_splits[9][1],range_splits[9][0]+1)
    m33 = rpyc.async_(m3.root.no_of_prime_numbers)(range_splits[10][1],range_splits[10][0]+1)
    m44 = rpyc.async_(m4.root.no_of_prime_numbers)(range_splits[11][1],range_splits[11][0]+1)

    n11 = rpyc.async_(n1.root.no_of_prime_numbers)(range_splits[12][1],range_splits[12][0]+1)
    n22 = rpyc.async_(n2.root.no_of_prime_numbers)(range_splits[13][1],range_splits[13][0]+1)
    n33 = rpyc.async_(n3.root.no_of_prime_numbers)(range_splits[14][1],range_splits[14][0]+1)
    n44 = rpyc.async_(n4.root.no_of_prime_numbers)(range_splits[15][1],range_splits[15][0]+1)

    o11 = rpyc.async_(o1.root.no_of_prime_numbers)(range_splits[16][1],range_splits[16][0]+1)
    o22 = rpyc.async_(o2.root.no_of_prime_numbers)(range_splits[17][1],range_splits[17][0]+1)
    o33 = rpyc.async_(o3.root.no_of_prime_numbers)(range_splits[18][1],range_splits[18][0]+1)
    o44 = rpyc.async_(o4.root.no_of_prime_numbers)(range_splits[19][1],range_splits[19][0]+1)
     
    t1 = time.time()
    pi1 = k11.ready == False and k22.ready == False and k33.ready == False and k44.ready == False
    pi2 = l11.ready == False and l22.ready == False and l33.ready == False and l44.ready == False
    pi3 = m11.ready == False and m22.ready == False and m33.ready == False and m44.ready == False
    pi4 = n11.ready == False and n22.ready == False and n33.ready == False and n44.ready == False
    pi5 = o11.ready == False and o22.ready == False and o33.ready == False and o44.ready == False

    while(pi1 == False and pi2 == False and pi3 == False and pi4 == False and pi5 == False):        
        pass

    pi1_sum = int(k11.value) + int(k22.value) + int(k33.value) + int(k44.value)
    pi2_sum = int(l11.value) + int(l22.value) + int(l33.value) + int(l44.value)
    pi3_sum = int(m11.value) + int(m22.value) + int(m33.value) + int(m44.value)
    pi4_sum = int(n11.value) + int(n22.value) + int(n33.value) + int(n44.value)
    pi5_sum = int(o11.value) + int(o22.value) + int(o33.value) + int(o44.value)

    result = f" Number of Prime Numbers : {pi1_sum + pi2_sum + pi3_sum + pi4_sum + pi5_sum} \n Time : {time.time() - t1} seconds "
    
    send_result('http://127.0.0.1:1880/PrimeFiveResult',result)

def PrimeOne(range_splits):   
    
    k1 = rpyc.connect('192.168.2.101',18861)  
    k2 = rpyc.connect('192.168.2.101',18862) 
    k3 = rpyc.connect('192.168.2.101',18863)
    k4 = rpyc.connect('192.168.2.101',18864)
    

    k11 = rpyc.async_(k1.root.no_of_prime_numbers)(range_splits[0][1],range_splits[0][0])
    k22 = rpyc.async_(k2.root.no_of_prime_numbers)(range_splits[1][1],range_splits[1][0]+1)
    k33 = rpyc.async_(k3.root.no_of_prime_numbers)(range_splits[2][1],range_splits[2][0]+1)
    k44 = rpyc.async_(k4.root.no_of_prime_numbers)(range_splits[3][1],range_splits[3][0]+1)
    
    t1 = time.time()
    pi1 = k11.ready == False and k22.ready == False and k33.ready == False and k44.ready == False
 

    while(pi1 == False):
        
        pass

    pi1_sum = int(k11.value) + int(k22.value) + int(k33.value) + int(k44.value)
    

    result = f"Number Of Prime Numbers: {pi1_sum} \n Time : {time.time() - t1} seconds   "    
    
    send_result('http://127.0.0.1:1880/PrimeOneResult',result)
    


def BruteFive(crypt_msg):     
    k1 = rpyc.connect('192.168.2.101',18861)
    l1 = rpyc.connect('192.168.2.102',18861)
    m1 = rpyc.connect('192.168.2.103',18861)
    n1 = rpyc.connect('192.168.2.104',18861)
    o1 = rpyc.connect('192.168.2.105',18861)

    k2 = rpyc.connect('192.168.2.101',18862)
    l2 = rpyc.connect('192.168.2.102',18862)
    m2 = rpyc.connect('192.168.2.103',18862)
    n2 = rpyc.connect('192.168.2.104',18862)
    o2 = rpyc.connect('192.168.2.105',18862)


    k3 = rpyc.connect('192.168.2.101',18863)
    l3 = rpyc.connect('192.168.2.102',18863)
    m3 = rpyc.connect('192.168.2.103',18863)
    n3 = rpyc.connect('192.168.2.104',18863)
    o3 = rpyc.connect('192.168.2.105',18863)


    k4 = rpyc.connect('192.168.2.101',18864)
    l4 = rpyc.connect('192.168.2.102',18864)
    m4 = rpyc.connect('192.168.2.103',18864)
    n4 = rpyc.connect('192.168.2.104',18864)
    o4 = rpyc.connect('192.168.2.105',18864)

    k11 = rpyc.async_(k1.root.decrypt)(crypt_msg,500,0)
    k22 = rpyc.async_(k2.root.decrypt)(crypt_msg,1000,500)
    k33 = rpyc.async_(k3.root.decrypt)(crypt_msg,1500,1000)
    k44 = rpyc.async_(k4.root.decrypt)(crypt_msg,2000,1500)

    l11 = rpyc.async_(l1.root.decrypt)(crypt_msg,2500,2000)
    l22 = rpyc.async_(l2.root.decrypt)(crypt_msg,3000,2500)
    l33 = rpyc.async_(l3.root.decrypt)(crypt_msg,3500,3000)
    l44 = rpyc.async_(l4.root.decrypt)(crypt_msg,4000,3500)

    m11 = rpyc.async_(m1.root.decrypt)(crypt_msg,4500,4000)
    m22 = rpyc.async_(m2.root.decrypt)(crypt_msg,5000,4500)
    m33 = rpyc.async_(m3.root.decrypt)(crypt_msg,5500,5000)
    m44 = rpyc.async_(m4.root.decrypt)(crypt_msg,6000,5500)

    n11 = rpyc.async_(n1.root.decrypt)(crypt_msg,6500,6000)
    n22 = rpyc.async_(n2.root.decrypt)(crypt_msg,7000,6500)
    n33 = rpyc.async_(n3.root.decrypt)(crypt_msg,7500,7000)
    n44 = rpyc.async_(n4.root.decrypt)(crypt_msg,8000,7500)

    o11 = rpyc.async_(o1.root.decrypt)(crypt_msg,8500,8000)
    o22 = rpyc.async_(o2.root.decrypt)(crypt_msg,9000,8500)
    o33 = rpyc.async_(o3.root.decrypt)(crypt_msg,9500,9000)
    o44 = rpyc.async_(o4.root.decrypt)(crypt_msg,10000,9500)

    workers = [[k11,k1],[k22,k2],[k33,k3],[k44,k4],[l11,l1],[l22,l2],[l33,l3],[l44,l4],[m11,m1],[m22,m2],[m33,m3],[m44,m4],[n11,n1],[n22,n2],[n33,n3],[n44,n4],[o11,o1],[o22,o2],[o33,o3],[o44,o4]]
    passowrd = 0
    t1 = time.time()
    flag = False
    while True:
        for i in range(0,20):
            if(workers[i][0].ready == True and workers[i][0].value[0] == True):
                passowrd = workers[i][0].value[1]                
                for i in workers:
                    i[1].close()
                flag = True
        if(flag):
            break
    result = f"Passowrd Found: {passowrd}....... Time Taken : {time.time()-t1}"    
    send_result('http://127.0.0.1:1880/DecryptFiveResult',result)


def BruteOne(crypt_msg):
    
    

    k1 = rpyc.connect('192.168.2.101',18861)  
    k2 = rpyc.connect('192.168.2.101',18862) 
    k3 = rpyc.connect('192.168.2.101',18863)
    k4 = rpyc.connect('192.168.2.101',18864)
    
    k11 = rpyc.async_(k1.root.decrypt)(crypt_msg,2500,0)
    k22 = rpyc.async_(k2.root.decrypt)(crypt_msg,5000,2500)
    k33 = rpyc.async_(k3.root.decrypt)(crypt_msg,7500,5000)
    k44 = rpyc.async_(k4.root.decrypt)(crypt_msg,10000,7500)

    workers = [[k11,k1],[k22,k2],[k33,k3],[k44,k4]]
    flag = False
    t1 = time.time()
    while True:
        for i in range(0,4):
            if(workers[i][0].ready == True and workers[i][0].value[0] == True):
                passowrd = workers[i][0].value[1]

                for i in workers:
                    i[1].close()
                flag = True
        if(flag):
            break
    result = f"Passowrd Found: {passowrd}...... Time Taken : {time.time()-t1}"
    
    print(result)
    send_result('http://127.0.0.1:1880/DecryptOneResult',result)

def send_result(http_url,result):
    http = httplib2.Http()
    http.request( http_url,'POST',result) 

def encrypt(msg,psw):        
    print(f"{msg}{psw}")
    msg_for_hash = msg.encode()
    hash_code = hashlib.sha1(msg_for_hash).hexdigest()
    enc_msg = []
    for i in range(len(msg)):
        enc_msg.append(chr(ord(msg[i]) + int((psw[i % len(psw)]))))
    enc_msg.append(hash_code)
    return enc_msg
def splitRange(lower_limit,upper_limit,num_of_splits):    
    cycles = 0    
    ranges = []
    k = 0        
    for i in range(int(lower_limit),int(upper_limit)+1):
        cycles = cycles + i

    equalized_cycles = int(cycles/num_of_splits)

    split_cycles = 0
    lower_limit_range = 0
    upper_limit_range = 0
    for i in range(int(lower_limit),int(upper_limit)+1):    
        split_cycles = split_cycles + i
        if(split_cycles >= equalized_cycles):
            upper_limit_range = i
            ranges.append([lower_limit_range,upper_limit_range])        
            lower_limit_range = i
            split_cycles = 0
            k = k+1

        if(k+1 == num_of_splits):
            ranges.append([lower_limit_range,int(upper_limit)])
            break
    return ranges


if __name__ == '__main__':
    app.run(host='0.0.0.0')
