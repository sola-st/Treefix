# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
if context.executing_eagerly():  # to_pyval only available in eager.
    st = st()  # Deferred init because it creates tensors.
    self.assertEqual(st.to_pyval(), expected)
