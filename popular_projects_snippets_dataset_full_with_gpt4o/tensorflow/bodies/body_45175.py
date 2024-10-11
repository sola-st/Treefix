# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
if not isinstance(inputs, tuple):
    inputs = (inputs,)
tr = self.transform(f, control_flow)
returns = tr(*inputs)
self.assertValuesEqual(returns, expected)
