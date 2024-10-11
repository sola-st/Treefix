# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli', 'show', '--dir', base_path,
    '--tag_set', 'badtagset'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with self.assertRaises(RuntimeError):
    saved_model_cli.show()
