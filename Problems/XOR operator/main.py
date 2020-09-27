def xor(a, b):
    if bool(a) == bool(b):
        return False
    return a if bool(a) else b