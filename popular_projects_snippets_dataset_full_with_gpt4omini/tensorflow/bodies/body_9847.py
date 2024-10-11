# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py

class DummyModel(autotrackable.AutoTrackable):
    """Model with callable polymorphic functions specified."""

    @def_function.function
    def func1(self, a, b, c):
        if c:
            exit(a + b)
        else:
            exit(a * b)

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=(2, 2), dtype=dtypes.float32)
    ])
    def func2(self, x):
        exit(x + 2)

    @def_function.function
    def __call__(self, y, c=7):
        exit(y + 2 * c)

    # Mocking _get_ops_in_metagraph because it returns a nondeterministically
    # ordered set of ops.
get_ops_mock.return_value = {'Op1'}
saved_model_dir = os.path.join(test.get_temp_dir(), 'dummy_model')
dummy_model = DummyModel()
# Call with specific values to create new polymorphic function traces.
dummy_model.func1(constant_op.constant(5), constant_op.constant(9), True)
dummy_model(constant_op.constant(5))
with self.cached_session():
    save.save(dummy_model, saved_model_dir)

exp_out = """MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['__saved_model_init_op']:
  The given SavedModel SignatureDef contains the following input(s):
  The given SavedModel SignatureDef contains the following output(s):
    outputs['__saved_model_init_op'] tensor_info:
        dtype: DT_INVALID
        shape: unknown_rank
        name: NoOp
  Method name is: 

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['x'] tensor_info:
        dtype: DT_FLOAT
        shape: (2, 2)
        name: serving_default_x:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['output_0'] tensor_info:
        dtype: DT_FLOAT
        shape: (2, 2)
        name: PartitionedCall:0
  Method name is: tensorflow/serving/predict
The MetaGraph with tag set ['serve'] contains the following ops: {'Op1'}

Concrete Functions:
  Function Name: '__call__'
    Option #1
      Callable with:
        Argument #1
          y: TensorSpec(shape=(), dtype=tf.int32, name='y')
        Argument #2
          DType: int
          Value: 7

  Function Name: 'func1'
    Option #1
      Callable with:
        Argument #1
          a: TensorSpec(shape=(), dtype=tf.int32, name='a')
        Argument #2
          b: TensorSpec(shape=(), dtype=tf.int32, name='b')
        Argument #3
          DType: bool
          Value: True

  Function Name: 'func2'
    Option #1
      Callable with:
        Argument #1
          x: TensorSpec(shape=(2, 2), dtype=tf.float32, name='x')
""".strip()  # pylint: enable=line-too-long

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS(
    ['saved_model_cli', 'show', '--dir', saved_model_dir, '--all'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, err):
    saved_model_cli.show()
output = out.getvalue().strip()
self.maxDiff = None  # Produce a useful error msg if the comparison fails
self.assertMultiLineEqual(output, exp_out)
self.assertEqual(err.getvalue().strip(), '')
