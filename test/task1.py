def return_unique_int_numbers(n):

    unique_int_numbers = list(set(n))
    unique_int_numbers.sort()
    print(unique_int_numbers)


return_unique_int_numbers([5, 12, 78, 4, 1, 1, 5, 5, 7, 5, 8, 8, 10, 0, 125])
return_unique_int_numbers([235, -12, 78.89, 47.85, 1, 1, 5, 5, 7, 5, 8, 8, 100, 0, 0, 125, 47.84])