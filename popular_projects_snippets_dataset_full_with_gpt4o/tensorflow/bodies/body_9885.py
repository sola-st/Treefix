# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
if not test.is_built_with_xla():
    self.skipTest('Skipping test because XLA is not compiled in.')

base_path = test.test_src_dir_path(SAVED_MODEL_PATH)
output_dir = os.path.join(test.get_temp_dir(), 'aot_compile_cpu_dir')

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'aot_compile_cpu', '--dir', base_path, '--tag_set', 'serve',
    '--output_prefix', output_dir, '--cpp_class', 'Compiled',
    '--signature_def_key', 'MISSING'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with self.assertRaisesRegex(ValueError, 'Unable to find signature_def'):
    saved_model_cli.aot_compile_cpu()
