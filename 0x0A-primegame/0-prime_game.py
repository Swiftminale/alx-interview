#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to determine the winner of the prime game."""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primesSet = sieve_of_eratosthenes(max_num)
    
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primes_in_game = [p for p in primesSet if p <= num]

        if not primes_in_game:
            benWinsCount += 1
            continue

        isMariaTurn = True

        while primes_in_game:
            smallestPrime = primes_in_game.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            if not roundsSet:
                if isMariaTurn:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            isMariaTurn = not isMariaTurn

    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif mariaWinsCount < benWinsCount:
        return "Ben"
    
    return None


def sieve_of_eratosthenes(n):
    """Returns a list of prime numbers up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(n ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

