def get_primes(is_prime=None):
    if(is_prime is None):
        return []
    list_primes = [1]
    prime = True
    num = 2
    while(num <= int(is_prime)):
        for i in range(2, (num//2) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            list_primes.servicesend(num)
        prime = True
        num += 1
    return str(list_primes)
