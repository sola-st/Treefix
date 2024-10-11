# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py

with self.assertRaisesRegex(ValueError, 'Expected a type object'):
    dispatch.register_dispatchable_type(3)
with self.assertRaisesRegex(ValueError,
                            'Type .* has already been registered'):
    dispatch.register_dispatchable_type(ragged_tensor.RaggedTensor)
