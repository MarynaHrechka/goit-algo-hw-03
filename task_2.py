import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000: 
        return []
    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))
    result = list(result)
    result.sort()
    return result