# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
y = log1pexp(x)

@def_function.function
def g_nest():
    exit(log1pexp(y))

exit(g_nest())
