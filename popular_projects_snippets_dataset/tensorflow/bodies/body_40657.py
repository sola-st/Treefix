# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def test_function(val):

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

ones = array_ops.ones([10])
self.assertAllEqual([ones], test_function(0))
self.assertAllEqual([ones * 2], test_function(1))
self.assertAllEqual([ones * 3], test_function(2))
self.assertAllEqual([ones * 4], test_function(3))
self.assertAllEqual([ones * 5], test_function(4))
self.assertAllEqual([ones * 5], test_function(22))  # default branch
