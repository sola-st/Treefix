# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)
input_path = os.path.join(test.get_temp_dir(), 'testRunCommand_inputs.npz')
x = np.array([[1], [2]])
x_notused = np.zeros((6, 3))
np.savez(input_path, x0=x, x1=x_notused)
output_file = os.path.join(test.get_temp_dir(), 'outputs.npy')
if os.path.exists(output_file):
    os.remove(output_file)

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'run', '--dir', base_path, '--tag_set', 'serve',
    '--signature_def', 'regress_x2_to_y3', '--inputs',
    'inputs=' + input_path + '[x0]', '--outdir', test.get_temp_dir()
    ] + (['--use_tfrt'] if use_tfrt else []))
parser = saved_model_cli.create_parser()
parser.parse_args()
saved_model_cli.run()
y_actual = np.load(output_file)
y_expected = np.array([[3.5], [4.0]])
self.assertAllClose(y_expected, y_actual)
