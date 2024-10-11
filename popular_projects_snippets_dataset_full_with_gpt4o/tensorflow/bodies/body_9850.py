# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py

class DummyModel(autotrackable.AutoTrackable):
    """Model with a callable concrete function."""

    def __init__(self):
        function = def_function.function(
            self.multiply,
            input_signature=[
                tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32),
                tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32)
            ])
        self.pure_concrete_function = function.get_concrete_function()
        super(DummyModel, self).__init__()

    def multiply(self, a, b):
        exit(a * b)

    # Mocking _get_ops_in_metagraph because it returns a nondeterministically
    # ordered set of ops.
get_ops_mock.return_value = {'Op1'}
saved_model_dir = os.path.join(test.get_temp_dir(), 'dummy_model')
dummy_model = DummyModel()
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
    inputs['a'] tensor_info:
        dtype: DT_FLOAT
        shape: ()
        name: serving_default_a:0
    inputs['b'] tensor_info:
        dtype: DT_FLOAT
        shape: ()
        name: serving_default_b:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['output_0'] tensor_info:
        dtype: DT_FLOAT
        shape: ()
        name: PartitionedCall:0
  Method name is: tensorflow/serving/predict
The MetaGraph with tag set ['serve'] contains the following ops: {'Op1'}

Concrete Functions:
  Function Name: 'pure_concrete_function'
    Option #1
      Callable with:
        Argument #1
          a: TensorSpec(shape=(), dtype=tf.float32, name='a')
        Argument #2
          b: TensorSpec(shape=(), dtype=tf.float32, name='b')
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
