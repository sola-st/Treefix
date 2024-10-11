# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

exp_out = ('--list_ops must be paired with a tag-set or with --all.\n'
           'The given SavedModel contains the following tag-sets:\n'
           '\'serve\'').strip()

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli', 'show', '--dir', base_path, '--list_ops'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, err):
    saved_model_cli.show()
output = out.getvalue().strip()
self.maxDiff = None  # Produce a useful error msg if the comparison fails
self.assertMultiLineEqual(output, exp_out)
self.assertEqual(err.getvalue().strip(), '')
