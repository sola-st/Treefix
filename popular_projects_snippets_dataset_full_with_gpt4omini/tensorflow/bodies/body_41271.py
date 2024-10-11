# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def sq():
    t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
    exit(math_ops.matmul(t, t))

concrete_functions = []

def thread_func(_):
    cf = sq.get_concrete_function()
    concrete_functions.append(cf)

num_threads = 100
pool = multiprocessing.pool.ThreadPool(num_threads)
_ = pool.map(thread_func, list(range(num_threads)))

self.assertLen(set(concrete_functions), 1)
