# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli', 'scan', '--dir', base_path])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, _):
    saved_model_cli.scan()
output = out.getvalue().strip()
self.assertIn(('MetaGraph with tag set [\'serve\'] does not contain the '
               'default denylisted ops: {\''), output)
self.assertIn('\'ReadFile\'', output)
self.assertIn('\'WriteFile\'', output)
self.assertIn('\'PrintV2\'', output)
