# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
"""Assert the two differnet methods (tensor_spec inputs or tensor inputs) experimental_get_compiler give same HLO text."""
flat_args = list(args) + list(kwargs.values())
if not all([isinstance(x, ops.Tensor) for x in flat_args]):
    self.skipTest('It only support args and kwargs are all tf.Tensor types.')

args_spec = nest.map_structure(tensor_spec.TensorSpec.from_tensor, args)
kwargs_spec = nest.map_structure(tensor_spec.TensorSpec.from_tensor, kwargs)

hlo_1 = f.experimental_get_compiler_ir(*args, **kwargs)()
hlo_2 = f.experimental_get_compiler_ir(*args_spec, **kwargs_spec)()

if hlo_1 != hlo_2:
    self.fail(
        'The tensor_spec way experimental_get_compiler_ir give diff result to'
        f' normal experimental_get_compiler_ir. \nhlo_1:\n{hlo_1}'
        f'\nhlo_2:\n{hlo_2}\n'
    )
