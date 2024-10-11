# Extracted from https://stackoverflow.com/questions/533905/how-to-get-the-cartesian-product-of-a-series-of-lists
def product(ar_list):
    if not ar_list:
        yield ()
    else:
        for a in ar_list[0]:
            for prod in product(ar_list[1:]):
                yield (a,)+prod

print list(product([[1,2],[3,4],[5,6]]))

[(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

