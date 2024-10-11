# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/common_test.py
a = constant_op.constant(10.0, name="a")
b = constant_op.constant(20.0, name="b")
c = constant_op.constant(30.0, name="c")
d = constant_op.constant(30.0, name="d")
run_key = common.get_run_key(
    {}, {"set1": [a, b], "set2": {"c": c, "d": d}})
loaded = json.loads(run_key)
self.assertItemsEqual([], loaded[0])
self.assertItemsEqual(["a:0", "b:0", "c:0", "d:0"], loaded[1])
