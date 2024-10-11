# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
nums = [1, 2, 3, 4, 5, 6]
elems = constant_op.constant(nums, name="data")
r = map_fn.map_fn(
    lambda x: math_ops.multiply(math_ops.add(x, 3), 2), elems)
self.assertAllEqual(
    np.array([(x + 3) * 2 for x in nums]), self.evaluate(r))
