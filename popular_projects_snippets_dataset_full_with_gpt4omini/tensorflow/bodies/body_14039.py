# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_pyval({"a": 5, "b": {"c": [1, 2, 3]}})
if context.executing_eagerly():
    expected = textwrap.dedent("""
          <StructuredTensor(
              fields={
                  "a": tf.Tensor(5, shape=(), dtype=int32),
                  "b": <StructuredTensor(
                          fields={
                              "c": tf.Tensor([1 2 3], shape=(3,), dtype=int32)},
                          shape=())>},
              shape=())>""")[1:]
else:
    expected = textwrap.dedent("""
          <StructuredTensor(
              fields={
                  "a": Tensor("Const:0", shape=(), dtype=int32),
                  "b": <StructuredTensor(
                          fields={
                              "c": Tensor("RaggedConstant/Const:0", shape=(3,), dtype=int32)},
                          shape=())>},
              shape=())>""")[1:]
self.assertEqual(repr(st), expected)
