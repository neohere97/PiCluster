import rpyc
import time
import httplib2
import requests
import threading
from flask import Flask,request

app = Flask(__name__)



@app.route('/runPrimeFivePi', methods=['POST'])
def FivePrime():
    t= threading.Thread(target=PrimeFive)
    t.start()
    return "OK"


@app.route('/runPrimeOnePi', methods=['POST'])
def OnePrime():
    t= threading.Thread(target=PrimeOne)
    t.start()            
    return "OK"

@app.route('/runBruteFivePi', methods=['POST'])
def FiveBrute():
    t= threading.Thread(target=BruteFive)
    t.start()
    return "OK"

@app.route('/runBruteOnePi', methods=['POST'])
def FiveBrute():
    t= threading.Thread(target=BruteOne)
    t.start()
    return "OK"
    

def PrimeFive():
    t1 = time.time()

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

    k11 = rpyc.async_(k1.root.no_of_prime_numbers)(25000,0)
    k22 = rpyc.async_(k2.root.no_of_prime_numbers)(33000,25000)
    k33 = rpyc.async_(k3.root.no_of_prime_numbers)(40000,33000)
    k44 = rpyc.async_(k4.root.no_of_prime_numbers)(45000,40000)

    l11 = rpyc.async_(l1.root.no_of_prime_numbers)(51000,45000)
    l22 = rpyc.async_(l2.root.no_of_prime_numbers)(55000,51000)
    l33 = rpyc.async_(l3.root.no_of_prime_numbers)(59000,55000)
    l44 = rpyc.async_(l4.root.no_of_prime_numbers)(63000,59000)

    m11 = rpyc.async_(m1.root.no_of_prime_numbers)(67000,63000)
    m22 = rpyc.async_(m2.root.no_of_prime_numbers)(70000,67000)
    m33 = rpyc.async_(m3.root.no_of_prime_numbers)(72000,70000)
    m44 = rpyc.async_(m4.root.no_of_prime_numbers)(74000,72000)

    n11 = rpyc.async_(n1.root.no_of_prime_numbers)(77000,74000)
    n22 = rpyc.async_(n2.root.no_of_prime_numbers)(81000,77000)
    n33 = rpyc.async_(n3.root.no_of_prime_numbers)(85000,81000)
    n44 = rpyc.async_(n4.root.no_of_prime_numbers)(88000,85000)

    o11 = rpyc.async_(o1.root.no_of_prime_numbers)(92000,88000)
    o22 = rpyc.async_(o2.root.no_of_prime_numbers)(95500,92000)
    o33 = rpyc.async_(o3.root.no_of_prime_numbers)(98000,95500)
    o44 = rpyc.async_(o4.root.no_of_prime_numbers)(100000,98000)


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
    
    http = httplib2.Http()    
    response, content = http.request( 'http://127.0.0.1:1880/PrimeFiveResult',
                                          'POST',
                                          result
                                      )

def PrimeOne():
    t1 = time.time()

    k1 = rpyc.connect('192.168.2.101',18861)  
    k2 = rpyc.connect('192.168.2.101',18862) 
    k3 = rpyc.connect('192.168.2.101',18863)
    k4 = rpyc.connect('192.168.2.101',18864)
    

    k11 = rpyc.async_(k1.root.no_of_prime_numbers)(45000,0)
    k22 = rpyc.async_(k2.root.no_of_prime_numbers)(70000,45000)
    k33 = rpyc.async_(k3.root.no_of_prime_numbers)(88000,70000)
    k44 = rpyc.async_(k4.root.no_of_prime_numbers)(100000,88000)
    

    pi1 = k11.ready == False and k22.ready == False and k33.ready == False and k44.ready == False
 

    while(pi1 == False):
        
        pass

    pi1_sum = int(k11.value) + int(k22.value) + int(k33.value) + int(k44.value)
    

    result = f"Number Of Prime Numbers: {pi1_sum} \n Time : {time.time() - t1} seconds   "    
    
    http = httplib2.Http()
    response, content = http.request( 'http://127.0.0.1:1880/PrimeOneResult',
                                          'POST',
                                          result) 


def BruteOne():

if __name__ == '__main__':
    app.run(host='0.0.0.0')
