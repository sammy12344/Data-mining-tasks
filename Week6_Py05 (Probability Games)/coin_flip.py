from numpy import random


def coin_toss(m):
    head_number = 0
    flip_count = 0
    while head_number < m:
        coin = random.randint(2)
        if coin == 1:
            head_number = head_number + 1
        flip_count = flip_count + 1

    return 2 * flip_count


m = 10
print(f"For {m} games, the average value is: {coin_toss(m)/m}")
m = 10000
print(f"For {m} games, the average value is: {coin_toss(m)/m}")
m = 1000000
print(f"For {m} games, the average value is: {coin_toss(m)/m}")
