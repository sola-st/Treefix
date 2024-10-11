# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'run', '--dir', base_path, '--tag_set', 'serve',
    '--signature_def', 'INVALID_SIGNATURE',
    '--input_exprs', 'x2=[1,2,3]'
    ] + (['--use_tfrt'] if use_tfrt else []))
parser = saved_model_cli.create_parser()
parser.parse_args()
with self.assertRaisesRegex(ValueError,
                            'Could not find signature '
                            '"INVALID_SIGNATURE"'):
    saved_model_cli.run()
