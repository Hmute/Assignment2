import urllib.request
import json
import time
import matplotlib.pyplot as plt

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Fetch the test data from the URL
url = ("https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json")
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

# Create a list to store the time it takes to run the function for each input
timing_results = []

for item in data:
    if type(item) == dict and "input" in item:
        input_data = item["input"]
        if type(input_data) == list:
            start_time = time.time()
            func1(input_data, 0, len(input_data) - 1)
            end_time = time.time()
            timing_results.append(end_time - start_time)

# Plot the timing results
plt.plot(timing_results)
plt.xlabel("Test Case Number")
plt.ylabel("Time (in seconds)")
plt.title("Time taken to sort an array using QuickSort")
plt.show()