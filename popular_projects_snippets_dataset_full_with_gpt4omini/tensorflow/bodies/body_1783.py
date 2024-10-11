# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
# x, y: f32[2, b, c]
x = np.arange(24, dtype=np.float32).reshape((2, 3, 4))
y = x

# Module takes two prefix arguments with the values of b and c
#   return (sin(x + y), x.shape[1])
module = """
module @jit_f.0 {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<i32>, %arg2: tensor<2x?x?xf32>, %arg3: tensor<2x?x?xf32>) -> (tensor<2x?x?xf32>, tensor<i32>) {
    %0 = stablehlo.add %arg2, %arg3 : tensor<2x?x?xf32>
    %1 = stablehlo.sine %0 : tensor<2x?x?xf32>
    return %1, %arg0 : tensor<2x?x?xf32>, tensor<i32>
  }
}
"""

dim_args_spec = ['0.1', '0.2']
def f(x, y):
    exit(xla.call_module([x, y],
                           version=2,
                           module=module,
                           Tout=[x.dtype, np.int32],
                           Sout=[(None, 3), ()],
                           dim_args_spec=dim_args_spec))
self._assertOpOutputMatchesExpected(f, (x, y), (np.sin(x + y), x.shape[1]))

dim_args_spec = ['0.0', '0.0', '0.0', '0.0']  # Too many dim_args_spec
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'The module should have 4 dimension arguments, '
    'but it has only 4 total arguments'):
    self._assertOpOutputMatchesExpected(f, (x, y),
                                        (np.sin(x + y), x.shape[1]))

dim_args_spec = ['0.0', '0.0', '0.0']  # dim_args_spec refers to non-scalar
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'Module argument at index 2 should be a 0-dimensional integer-tensor '
    'dimension argument but has type'):
    self._assertOpOutputMatchesExpected(f, (x, y),
                                        (np.sin(x + y), x.shape[1]))

dim_args_spec = []  # No dim_args_spec
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'Module main has dynamic shapes but no dim_args_spec was given'):
    self._assertOpOutputMatchesExpected(f, (x, y),
                                        (np.sin(x + y), x.shape[1]))

dim_args_spec = ['1.0']  # Too few dim_args_spec
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'Incorrect number of arguments for XlaCallModule: 2. '
    'The module has 4 of which 1 were declared to be dimension arguments.'):
    self._assertOpOutputMatchesExpected(f, (x, y),
                                        (np.sin(x + y), x.shape[1]))

dim_args_spec = ['0.b', '0.1']  # axis_idx not a number
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Syntax error in dim_args_spec '0.b'"):
    self._assertOpOutputMatchesExpected(f, (x, y),
                                        (np.sin(x + y), x.shape[1]))

dim_args_spec = ['2.0', '0.1']  # arg_idx too large
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'Invalid argument index 2 when the number of non-dimension arguments '
    "is 2 in dim_arg_spec '2.0'"):
    self._assertOpOutputMatchesExpected(f, (x, y),
                                        (np.sin(x + y), x.shape[1]))

dim_args_spec = ['0.3', '0.1']  # axis_idx too large
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'Invalid axis index 3 when the rank of non-dimension argument 0 '
    "is 3 in dim_arg_spec '0.3'"):
    self._assertOpOutputMatchesExpected(f, (x, y),
                                        (np.sin(x + y), x.shape[1]))
