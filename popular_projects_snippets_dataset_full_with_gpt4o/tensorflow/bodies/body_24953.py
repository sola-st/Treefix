# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/common_test.py
a = constant_op.constant(10.0, name="a")
b = constant_op.constant(20.0, name="b")
run_key = common.get_run_key({"a": a}, [a, b])
loaded = json.loads(run_key)
self.assertItemsEqual(["a:0"], loaded[0])
self.assertItemsEqual(["a:0", "b:0"], loaded[1])
