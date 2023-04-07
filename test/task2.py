def calc_cosine_distance(l1, l2):

    p1 = sum([x * y for x, y in zip(l1, l2)])
    p2 = sum([abs(x ** 2) for x in l1])
    p3 = sum([abs(y ** 2) for y in l2])
    sqrt = (p2 * p3) ** 0.5
    cosine_distance = round((1 - p1/sqrt), 5)

    print(cosine_distance)


l1 = [1, 1, 1, 1, 1, 0, 0, 1]
l2 = [0, 0, 1, 1, 0, 1, 1, 1]

d1 = [7, 200, 15]
d2 = [7, 200, 20]

v1 = [1, 2, 3]
v2 = [4, 5, 6]

calc_cosine_distance(l1, l2)
calc_cosine_distance(d1, d2)
calc_cosine_distance(v1, v2)