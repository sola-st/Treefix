# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

exp_header = ('The given SavedModel MetaGraphDef contains SignatureDefs '
              'with the following keys:')
exp_start = 'SignatureDef key: '
exp_keys = [
    '"classify_x2_to_y3"', '"classify_x_to_y"', '"regress_x2_to_y3"',
    '"regress_x_to_y"', '"regress_x_to_y2"', '"serving_default"'
]

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS(
    ['saved_model_cli', 'show', '--dir', base_path, '--tag_set', 'serve'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, err):
    saved_model_cli.show()
output = out.getvalue().strip()
# Order of signatures does not matter
self.assertMultiLineEqual(
    output,
    '\n'.join([exp_header] +
              [exp_start + exp_key for exp_key in exp_keys]))
self.assertEqual(err.getvalue().strip(), '')
