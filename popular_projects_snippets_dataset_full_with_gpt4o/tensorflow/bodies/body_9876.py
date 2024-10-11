# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)
output_dir = os.path.join(test.get_temp_dir(), 'new_dir')

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'run', '--dir', base_path, '--tag_set', 'serve',
    '--signature_def', 'regress_x_to_y',
    '--input_examples', 'inputs={"x":8.0,"x2":5.0}',
    '--outdir', output_dir
    ] + (['--use_tfrt'] if use_tfrt else []))
parser = saved_model_cli.create_parser()
parser.parse_args()
with self.assertRaisesRegex(ValueError, 'must be a list'):
    saved_model_cli.run()
