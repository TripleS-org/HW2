"""
Module for generating a shuffled array.
"""
import secrets

def random_array(arr):
    """Fills array with random numbers."""
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(21)
    return arr
