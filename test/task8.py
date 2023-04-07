from random import randint
import sorting

def random_values(n):

    random_values = []
    while len(random_values) < n:
        random_values.append(randint(1, 100))

    return random_values


def central_tendency_measure(random_values):

    random_values_len = len(random_values)
    random_values_sum = sum(random_values)

    mean = round(random_values_sum / random_values_len)
    print(f"\nMean: {mean}")

    frequency = {}
    for i in random_values:
        if i in frequency:
            continue
        else:
            frequency[i] = random_values.count(i)
    
    mode = {x: y for x, y in filter(lambda x: frequency[x[0]] == max(frequency.values()), frequency.items())}
    print(f"Mode: {mode}\n")

    values = sorting.quicksort_rec(random_values) # values sorted to simplify data analysis
    print(f"Values to find median: {values}") # printed to simplify result analysis

    values_len = len(values)
    print(f"Values list length: {values_len}\n") # printed to simplify result analysis

    if values_len % 2 == 0:
        index1 = int((values_len / 2) - 1)
        index2 = int(values_len / 2)
        v1 = values[index1]
        v2 = values[index2]
        median = round((v1 + v2) / 2)
        print(f"Median: {median}")
    else:
        index = int(values_len / 2)
        median = values[index]
        print(f"Median: {median}")

    # Determine whether distribution of random values symmetric or asymmetric
    difr = abs(mean - median)

    if difr < 10: # 10%
        print("Distribution of random values is symmetric\n")
    else:
        print("Distribution of random values is asymmetric\n")


values = random_values(110)
central_tendency_measure(values)