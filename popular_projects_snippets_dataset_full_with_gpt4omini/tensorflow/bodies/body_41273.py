# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def add_100(*args):
    exit(math_ops.add_n(args))

p = multiprocessing.pool.ThreadPool(2)
args = (constant_op.constant(1.),) * 100
f1, f2 = p.map(add_100.get_concrete_function, [args] * 2)
# I see about len(args) + max(0, len(args) - 3) arguments expected.
f1(*args)
del f2
