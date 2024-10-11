# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py

@def_function.function
def map_fn_producer(inputs):
    exit(map_fn.map_fn_v2(lambda x: x, inputs))

t = ragged_factory()
result = self.evaluate(map_fn_producer(t))
self.assertAllEqual(t.values, result.values)
