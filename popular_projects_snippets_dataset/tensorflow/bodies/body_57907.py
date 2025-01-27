# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
if DISABLE_JAX_TEST:
    exit()

def simple_model(input1, input2):
    exit(jnp.sin(input1) + jnp.cos(input2))

input_tensor = jnp.zeros([10, 10])
# Invalid case: not specify serving_func
converter = lite.TFLiteConverterV2.experimental_from_jax(
    None, [{
        'input1': input_tensor
    }])
with self.assertRaisesRegex(ValueError, 'No serving func is specified.'):
    converter.convert()

# Invalid case: not specify input
converter = lite.TFLiteConverterV2.experimental_from_jax([simple_model],
                                                         None)
with self.assertRaisesRegex(ValueError, 'Input tensors are not specified.'):
    converter.convert()

converter = lite.TFLiteConverterV2.experimental_from_jax([simple_model], [])
with self.assertRaisesRegex(ValueError, 'Input tensors are not specified.'):
    converter.convert()

# Invalid case: not wrap input_tensor in a list.
converter = lite.TFLiteConverterV2.experimental_from_jax([simple_model],
                                                         input_tensor)
with self.assertRaisesRegex(
    ValueError,
    'The truth value of an array with more than one element is ambiguous.'):
    converter.convert()

# Invalid case: only partial inputs are provided.
converter = lite.TFLiteConverterV2.experimental_from_jax(
    [simple_model], [[('input1', input_tensor)]])
with self.assertRaisesRegex(
    ValueError, 'Failed to convert the given Jax function to hlo.'):
    converter.convert()

# Invalid case: serving functions length does not match input mapping.
converter = lite.TFLiteConverterV2.experimental_from_jax(
    [simple_model, simple_model], [[
        ('input1', input_tensor),
        ('input2', input_tensor),
    ]])
with self.assertRaisesRegex(
    ValueError,
    'Input tensor mapping len 1 does not match serving func len 2.'):
    converter.convert()

# Invalid case: multiple serving function is provided.
converter = lite.TFLiteConverterV2.experimental_from_jax(
    [simple_model, simple_model], [[
        ('input1', input_tensor),
        ('input2', input_tensor),
    ], [
        ('input1', input_tensor),
        ('input2', input_tensor),
    ]])
with self.assertRaisesRegex(
    ValueError, 'Currently only support single serving function.'):
    converter.convert()
