"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    cnt = 1
    curNo = 2
    while cnt < number_of_primes:
        curNo += 1
        prime = True
        for i in range(2,curNo):
            if curNo % i == 0:
                prime = False
        if prime:
            cnt+=1
            list.append(curNo)
    return list

print(primes(10))
