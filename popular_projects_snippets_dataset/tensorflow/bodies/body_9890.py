# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
if not test.is_built_with_xla():
    self.skipTest('Skipping test because XLA is not compiled in.')

saved_model_dir = os.path.join(test.get_temp_dir(), 'dummy_model')
dummy_model = self.AOTCompileDummyModel()
func = getattr(dummy_model, func)
with self.cached_session():
    self.evaluate(dummy_model.var.initializer)
    self.evaluate(dummy_model.write_var.initializer)
    save.save(dummy_model, saved_model_dir, signatures={'func': func})

output_prefix = os.path.join(test.get_temp_dir(), 'aot_compile_cpu_dir/out')

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli',  # Use the default serving signature_key.
    'aot_compile_cpu', '--dir', saved_model_dir, '--tag_set', 'serve',
    '--signature_def_key', 'func', '--output_prefix', output_prefix,
    '--variables_to_feed', variables_to_feed,
    '--cpp_class', 'Generated'
    ] + (['--target_triple', target_triple] if target_triple else []))
parser = saved_model_cli.create_parser()
parser.parse_args()
with test.mock.patch.object(logging, 'warn') as captured_warn:
    saved_model_cli.aot_compile_cpu()
self.assertRegex(
    str(captured_warn.call_args),
    'Signature input key \'y\'.*has been pruned while freezing the '
    'graph.')
self.assertTrue(file_io.file_exists('{}.o'.format(output_prefix)))
self.assertTrue(file_io.file_exists('{}.h'.format(output_prefix)))
self.assertTrue(file_io.file_exists(
    '{}_metadata.o'.format(output_prefix)))
self.assertTrue(
    file_io.file_exists('{}_makefile.inc'.format(output_prefix)))
header_contents = file_io.read_file_to_string(
    '{}.h'.format(output_prefix))
self.assertIn('class Generated', header_contents)
self.assertIn('arg_feed_x_data', header_contents)
self.assertIn('result_fetch_res_data', header_contents)
# arg_y got filtered out as it's not used by the output.
self.assertNotIn('arg_feed_y_data', header_contents)
if variables_to_feed:
    # Read-only-variables' setters preserve constness.
    self.assertIn('set_var_param_my_var_data(const float', header_contents)
    self.assertNotIn('set_var_param_my_var_data(float', header_contents)
if func == dummy_model.func_write:  # pylint: disable=comparison-with-callable
    # Writeable variables setters do not preserve constness.
    self.assertIn('set_var_param_write_var_data(float', header_contents)
    self.assertNotIn('set_var_param_write_var_data(const float',
                     header_contents)

makefile_contents = file_io.read_file_to_string(
    '{}_makefile.inc'.format(output_prefix))
self.assertIn('-D_GLIBCXX_USE_CXX11_ABI=', makefile_contents)
