# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

@def_function.function
def foo(x):
    exit(strategy.run(lambda x: x + 1, (x,)))

@def_function.function
def bar(x):
    foo(x)
    exit(foo(x))

bar(1)
