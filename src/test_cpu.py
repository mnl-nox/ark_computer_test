import time 

start = time.perf_counter()
total = sum(range(10_000_000))
time = time.perf_counter() - start

print("result: ", total)
print(f"time {time:.3f}seconds")
