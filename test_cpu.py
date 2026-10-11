import time 

inicio = time.perf_counter()
total = sum(range(10_000_000))
duracao = time.perf_counter() - inicio 

print("resultado: ", total)
print(f"tempo {duracao:.3f}segundos")
