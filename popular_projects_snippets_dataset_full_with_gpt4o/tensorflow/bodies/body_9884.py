# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'scan', '--dir', base_path, '--tag_set', 'serve', '--op_denylist',
    'VariableV2,Assign,Relu6'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, _):
    saved_model_cli.scan()
output = out.getvalue().strip()
self.assertIn(('MetaGraph with tag set [\'serve\'] contains the following'
               ' denylisted ops:'), output)
self.assertTrue(('{\'VariableV2\', \'Assign\'}' in output) or
                ('{\'Assign\', \'VariableV2\'}' in output))
