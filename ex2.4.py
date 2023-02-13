import sys
import json
import time
import matplotlib.pyplot as plt
import urllib.request
import random

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

# def func2(array, start, end):
#     p = array[start]
#     low = start + 1
#     high = end
#     while True:
#         while low <= high and array[high] >= p:
#             high = high - 1
#         while low <= high and array[low] <= p:
#             low = low + 1
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#         else:
#             break
#     array[start], array[high] = array[high], array[start]
#     return high

def func2(arr, low, high):
    i = (low - 1)
    pivot = arr[int((low + high) / 2)]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def test_quick_sort(inputs):
    results = []
    for arr in inputs:
        start = time.time()
        func1(arr, 0, len(arr)-1)
        end = time.time()
        results.append(end - start)
        print(results)
    return results

def plot_results(results):
    x = list(range(0, len(results)))
    plt.plot(x, results, label="Quick Sort")
    plt.xlabel("Input (n)")
    plt.ylabel("Time (s)")
    plt.title("Comparison of Quick Sort Times")
    plt.legend()
    plt.show()

def fetch_inputs():
    url = ("https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json")
    response = urllib.request.urlopen(url) 
    inputs = json.loads(response.read().decode()) 
    # randomize the inputs
    for i in range(len(inputs)):
        random.shuffle(inputs[i])

    return inputs

if __name__ == "__main__":
    inputs = fetch_inputs()
    results = test_quick_sort(inputs)
    print(results)
    plot_results(results)

