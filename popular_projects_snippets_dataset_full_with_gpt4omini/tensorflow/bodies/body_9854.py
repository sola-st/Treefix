# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

expected_output = (
    'The given SavedModel SignatureDef contains the following input(s):\n'
    '  inputs[\'x\'] tensor_info:\n'
    '      dtype: DT_FLOAT\n      shape: (-1, 1)\n      name: x:0\n'
    'The given SavedModel SignatureDef contains the following output(s):\n'
    '  outputs[\'y\'] tensor_info:\n'
    '      dtype: DT_FLOAT\n      shape: (-1, 1)\n      name: y:0\n'
    'Method name is: tensorflow/serving/predict')

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli', 'show', '--dir', base_path, '--tag_set', 'serve',
    '--signature_def', 'serving_default'
])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, err):
    saved_model_cli.show()
output = out.getvalue().strip()
self.assertEqual(output, expected_output)
self.assertEqual(err.getvalue().strip(), '')
