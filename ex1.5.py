import time
import matplotlib.pyplot as plt

def original_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_fib(n-1) + original_fib(n-2)
        
def optimized_fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = optimized_fib(n-1, memo) + optimized_fib(n-2, memo)
        return memo[n]

times_original = []
times_optimized = []

for i in range(36):
    start = time.time()
    original_fib(i)
    end = time.time()
    times_original.append(end - start)
    
    start = time.time()
    optimized_fib(i)
    end = time.time()
    times_optimized.append(end - start)

print("Original times:", times_original)
print("Optimized times:", times_optimized)

original_times = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009970664978027344, 0.0, 0.0, 0.0, 0.0009970664978027344, 0.000997304916381836, 0.002575397491455078, 0.0030341148376464844, 0.0049474239349365234, 0.008591413497924805, 0.016687393188476562, 0.027419567108154297, 0.043982744216918945, 0.06977152824401855, 0.11191534996032715, 0.14805912971496582, 0.24490666389465332, 0.44362473487854004, 0.6535837650299072, 1.0557434558868408, 1.6206433773040771, 2.7429776191711426]
optimized_times = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

x = list(range(0, 36))

plt.plot(x, original_times, label="Original")
plt.plot(x, optimized_times, label="Optimized")

plt.xlabel("Input (n)")
plt.ylabel("Time (s)")
plt.title("Comparison of Original and Optimized Times")

plt.legend()
plt.show()