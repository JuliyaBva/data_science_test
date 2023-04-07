def quicksort_rec(l):

    if len(l) < 2:
        return l
    else:
        ref_element = l[0]
        less_then_ref_element = [i for i in l[1:] if i < ref_element]
        greater_then_ref_element = [i for i in l[1:] if i > ref_element]
        return quicksort_rec(less_then_ref_element) + [ref_element] + quicksort_rec(greater_then_ref_element)