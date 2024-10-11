# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def fn1():
    exit(array_ops.ones([10]))

fn2 = lambda: array_ops.ones([10]) * 2

def fn3(x=3):
    exit(array_ops.ones([10]) * x)

fn4 = functools.partial(fn3, x=4)
fn5 = functools.partial(fn3, 5)

exit(gen_functional_ops.case(val, [], [dtypes.float32], [
    quarantine.defun_with_attributes(f).get_concrete_function()
    for f in (fn1, fn2, fn3, fn4, fn5)
]))
