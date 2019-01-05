import rpyc
import time

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

k11 = rpyc.async_(k1.root.no_of_prime_numbers)(18000,0)
# k22 = rpyc.async_(k2.root.no_of_prime_numbers)(11000,6000)
# k33 = rpyc.async_(k3.root.no_of_prime_numbers)(15000,11000)
# k44 = rpyc.async_(k4.root.no_of_prime_numbers)(18000,15000)

l11 = rpyc.async_(l1.root.no_of_prime_numbers)(30000,18000)
# l22 = rpyc.async_(l2.root.no_of_prime_numbers)(200,22000)
# l33 = rpyc.async_(l3.root.no_of_prime_numbers)(5600,5100)
# l44 = rpyc.async_(l4.root.no_of_prime_numbers)(6000,5600)

m11 = rpyc.async_(m1.root.no_of_prime_numbers)(38000,30000)
# m22 = rpyc.async_(m2.root.no_of_prime_numbers)(6900,6500)
# m33 = rpyc.async_(m3.root.no_of_prime_numbers)(7200,6900)
# m44 = rpyc.async_(m4.root.no_of_prime_numbers)(7500,7200)

n11 = rpyc.async_(n1.root.no_of_prime_numbers)(45000,38000)
# n22 = rpyc.async_(n2.root.no_of_prime_numbers)(37000,34000)
# n33 = rpyc.async_(n3.root.no_of_prime_numbers)(40000,37000)
# n44 = rpyc.async_(n4.root.no_of_prime_numbers)(42000,40000)

o11 = rpyc.async_(o1.root.no_of_prime_numbers)(50000,45000)
# o22 = rpyc.async_(o2.root.no_of_prime_numbers)(47500,4500)
# o33 = rpyc.async_(o3.root.no_of_prime_numbers)(49000,47500)
# o44 = rpyc.async_(o4.root.no_of_prime_numbers)(50000,49000)


pi1 = k11.ready == False
#  and k22.ready == False and k33.ready == False and k44.ready == False
pi2 = l11.ready == False 
# and l22.ready == False and l33.ready == False and l44.ready == False
pi3 = m11.ready == False
#  and m22.ready == False and m33.ready == False and m44.ready == False
pi4 = n11.ready == False 
# and n22.ready == False and n33.ready == False and n44.ready == False
pi5 = o11.ready == False
#  and o22.ready == False and o33.ready == False and o44.ready == False

while(pi1 == False and pi2 == False and pi3 == False and pi4 == False and pi5 == False):
    print(f"pi1:{pi1}  \n pi2:{pi2}  \npi3:{pi3}  \npi4:{pi4}  \npi5:{pi5}  \n")
    pass

pi1_sum = int(k11.value) 
# + int(k22.value) + int(k33.value) + int(k44.value)
pi2_sum = int(l11.value) 
# + int(l22.value) + int(l33.value) + int(l44.value)
pi3_sum = int(m11.value)
#  + int(m22.value) + int(m33.value) + int(m44.value)
pi4_sum = int(n11.value) 
# + int(n22.value) + int(n33.value) + int(n44.value)
pi5_sum = int(o11.value) 
# + int(o22.value) + int(o33.value) + int(o44.value)

print(f" \n \n number of prime numbers in the range : {pi1_sum + pi2_sum + pi3_sum + pi4_sum + pi5_sum} time taken : {time.time() - t1} \n \n ")

