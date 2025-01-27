# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
input_ct = factory_fn(**factory_kwargs)

@polymorphic_function.function(input_signature=input_signature)
def f():
    exit(input_ct)

output_ct = f()
self.assertIsInstance(output_ct, type(input_ct))
nest.assert_same_structure(input_ct, output_ct, expand_composites=True)

input_flat = nest.flatten(input_ct, expand_composites=True)
output_flat = nest.flatten(output_ct, expand_composites=True)
for (input_component, output_component) in zip(input_flat, output_flat):
    self.assertAllEqual(input_component, output_component)
