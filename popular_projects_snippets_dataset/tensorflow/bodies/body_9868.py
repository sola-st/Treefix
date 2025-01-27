# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)
output_dir = os.path.join(test.get_temp_dir(),
                          'input_examples' + ('tfrt' if use_tfrt else ''))

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'run', '--dir', base_path, '--tag_set', 'serve',
    '--signature_def', 'regress_x_to_y', '--input_examples',
    'inputs=[{"x":[8.0],"x2":[5.0]}, {"x":[4.0],"x2":[3.0]}]',
    '--outdir', output_dir
    ] + (['--use_tfrt'] if use_tfrt else []))
parser = saved_model_cli.create_parser()
parser.parse_args()
saved_model_cli.run()
y_actual = np.load(os.path.join(output_dir, 'outputs.npy'))
y_expected = np.array([[6.0], [4.0]])
self.assertAllEqual(y_expected, y_actual)
