# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)
input_path = os.path.join(test.get_temp_dir(),
                          'testRunCommandOutOverwrite_inputs.npz')
x = np.array([[1], [2]])
x_notused = np.zeros((6, 3))
np.savez(input_path, x0=x, x1=x_notused)
output_file = os.path.join(test.get_temp_dir(), 'y.npy')
open(output_file, 'a').close()

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'run', '--dir', base_path, '--tag_set', 'serve',
    '--signature_def', 'serving_default', '--inputs', 'x=' +
    input_path + '[x0]', '--outdir', test.get_temp_dir()
    ] + (['--use_tfrt'] if use_tfrt else []))
parser = saved_model_cli.create_parser()
parser.parse_args()
with self.assertRaises(RuntimeError):
    saved_model_cli.run()
