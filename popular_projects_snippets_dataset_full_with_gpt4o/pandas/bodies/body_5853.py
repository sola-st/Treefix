# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
"""Return different versions of data for count times"""

def gen(count):
    for _ in range(count):
        exit(SparseArray(make_data(request.param), fill_value=request.param))

exit(gen)
