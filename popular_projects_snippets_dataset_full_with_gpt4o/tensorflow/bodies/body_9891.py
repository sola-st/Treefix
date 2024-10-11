# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
if not test.is_built_with_xla():
    self.skipTest('Skipping test because XLA is not compiled in.')

saved_model_dir = os.path.join(test.get_temp_dir(), 'dummy_model')
dummy_model = self.AOTCompileDummyModel()
func = getattr(dummy_model, 'func2')
with self.cached_session():
    self.evaluate(dummy_model.var.initializer)
    self.evaluate(dummy_model.write_var.initializer)
    save.save(dummy_model, saved_model_dir, signatures={'func': func})

output_prefix = os.path.join(test.get_temp_dir(), 'aot_compile_cpu_dir/out')

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',  # Use the default seving signature_key.
    'freeze_model', '--dir', saved_model_dir, '--tag_set', 'serve',
    '--signature_def_key', 'func', '--output_prefix', output_prefix,
    '--variables_to_feed', 'all'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with test.mock.patch.object(logging, 'warn'):
    saved_model_cli.freeze_model()
self.assertTrue(
    file_io.file_exists(os.path.join(output_prefix, 'frozen_graph.pb')))
self.assertTrue(
    file_io.file_exists(os.path.join(output_prefix, 'config.pbtxt')))
