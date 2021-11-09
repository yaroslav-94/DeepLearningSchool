import time
a = 1_000_000_000
t = time.time()
while a>0:
    a -= 1
print(time.time()-t)