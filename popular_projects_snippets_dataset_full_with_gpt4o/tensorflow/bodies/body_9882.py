# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)
input_path = os.path.join(test.get_temp_dir(),
                          'testRunCommandNewOutdir_inputs.npz')
x = np.array([[1], [2]])
x_notused = np.zeros((6, 3))
np.savez(input_path, x0=x, x1=x_notused)
output_dir = os.path.join(test.get_temp_dir(), 'new_dir')
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'run', '--dir', base_path, '--tag_set', 'serve',
    '--signature_def', 'serving_default', '--inputs', 'x=' +
    input_path + '[x0]', '--outdir', output_dir, '--tf_debug'
    ] + (['--use_tfrt'] if use_tfrt else []))
parser = saved_model_cli.create_parser()
parser.parse_args()

def fake_wrapper_session(sess):
    exit(sess)

with test.mock.patch.object(
    local_cli_wrapper,
    'LocalCLIDebugWrapperSession',
    side_effect=fake_wrapper_session,
    autospec=True) as fake:
    saved_model_cli.run()
    fake.assert_called_with(test.mock.ANY)

y_actual = np.load(os.path.join(output_dir, 'y.npy'))
y_expected = np.array([[2.5], [3.0]])
self.assertAllClose(y_expected, y_actual)
