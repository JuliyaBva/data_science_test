import sorting
from words_dictionary import words_dictionary

def search_query_distribution(sq):

    sq_list = []
    words_count_list = []
    percentage_list = []
    res_list = []
    
    for i in sq:
        c = len(i.split())
        sq_list.append(c)

    sq_sorted = sorting.quicksort_rec(sq_list)
    n = len(sq_list)

    for i in sq_sorted:
        words_count = sq_list.count(i)
        words_count_list.append(words_count)

        percentage = round((words_count / n) * 100)
        percentage_list.append(percentage)

    words = [f"{x} {value}" for x in sq_sorted for key, value in words_dictionary.items() if x == key] # only for number of words < 10

    for x, y in zip(words, percentage_list):
        res = (f"{x}: {y}%")
        res_list.append(res)
    
    res = ""
    for i in res_list:
        res = f"{res}{i}\n"
    
    print(res)


search_queries = ["watch new movies",
                  "coffee near me",
                  "how to find the determinant",
                  "python",
                  "data science jobs in UK",
                  "courses for data science",
                  "taxi",
                  "google",
                  "yandex",
                  "bing",
                  "foreign exchange rates USD/BYN",
                  "Netflix movies watch online free",
                  "Statistics courses online from top universities"]


search_query_distribution(search_queries)