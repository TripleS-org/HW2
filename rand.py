
import random
import secrets

def random_array(arr):

    shuffled_num = None
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(21)
    return arr
