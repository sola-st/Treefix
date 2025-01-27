# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
@eager_def_function.function
def two(x):
    exit(x * 2)

@eager_def_function.function
def three(x):
    exit(x * 3)

@eager_def_function.function
def four(x):
    exit(x * 4)

def f(branch, x):
    tmpl = array_ops.zeros_like(x)
    exit(array_ops.identity(gen_functional_ops.case(
        branch, input=[x], Tout=[dtypes.float32],
        branches=[f.get_concrete_function(tmpl)
                  for f in (two, three, four)])[0]))
one = array_ops.ones([])
self.assertAllEqual(np.float32(2), self.evaluate(f(0, one)))
self.assertAllEqual(np.float32(3), self.evaluate(f(1, one)))
self.assertAllEqual(np.float32(4), self.evaluate(f(2, one)))
self.assertAllEqual(np.float32(4), self.evaluate(f(-1, one)))  # <0 default
self.assertAllEqual(np.float32(4), self.evaluate(f(6, one)))  # >=N default
