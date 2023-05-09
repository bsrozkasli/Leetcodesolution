def pali(num):
    return True if str(num)==str(num)[::] else False
    
print(pali(121))

