# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
# Mocking _get_ops_in_metagraph because it returns a nondeterministically
# ordered set of ops.
get_ops_mock.return_value = {'Op1', 'Op2', 'Op3'}
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

# pylint: disable=line-too-long
exp_out = """MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['classify_x2_to_y3']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: x2:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['scores'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: y3:0
  Method name is: tensorflow/serving/classify

signature_def['classify_x_to_y']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_STRING
        shape: unknown_rank
        name: tf_example:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['scores'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: y:0
  Method name is: tensorflow/serving/classify

signature_def['regress_x2_to_y3']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: x2:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['outputs'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: y3:0
  Method name is: tensorflow/serving/regress

signature_def['regress_x_to_y']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_STRING
        shape: unknown_rank
        name: tf_example:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['outputs'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: y:0
  Method name is: tensorflow/serving/regress

signature_def['regress_x_to_y2']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_STRING
        shape: unknown_rank
        name: tf_example:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['outputs'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: y2:0
  Method name is: tensorflow/serving/regress

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['x'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: x:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['y'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: y:0
  Method name is: tensorflow/serving/predict
The MetaGraph with tag set ['serve'] contains the following ops:"""
# pylint: enable=line-too-long

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS(
    ['saved_model_cli', 'show', '--dir', base_path, '--all'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, err):
    saved_model_cli.show()
get_ops_mock.assert_called_once()
output = out.getvalue().strip()
self.maxDiff = None  # Produce useful error msg if the comparison fails
self.assertIn(exp_out, output)
self.assertIn('Op1', output)
self.assertIn('Op2', output)
self.assertIn('Op3', output)
self.assertEqual(err.getvalue().strip(), '')
