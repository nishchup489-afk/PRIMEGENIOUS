# n = int(input("Enter your number:  "))

# to exclude 
# 1) `2`
# 2) `3` better if you do so 
# 3) odd numbers , even numbers cant be prime
# 4) number greater than i^2
# 5) non-divisible

def get_prime_factors(inp):
    numbers = []


    while inp%2 == 0:   # excluded 2
        numbers.append(2)
        inp//=2
    
    while inp%3 == 0:   # excluded 3
        numbers.append(3)
        inp//=3

    i = 5 
    while i*i <=inp:     # excluded i^2
        while inp%i == 0: # excluded non divisible
            numbers.append(i)
            inp //=i
        i+=2             # excluded even

    if (inp > 1):
        numbers.append(inp)
    return numbers

print(get_prime_factors(91))