# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/common.py
"""Function passed to absl.app.run."""
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
if FLAGS.save_model_path:
    save_model_path = FLAGS.save_model_path
else:
    save_model_path = tempfile.mkdtemp(suffix='.saved_model')
save_options = tf.saved_model.SaveOptions(save_debug_info=show_debug_info)
tf.saved_model.save(
    create_module_fn(), save_model_path, options=save_options)
logging.info('Saved model to: %s', save_model_path)
mlir = pywrap_mlir.experimental_convert_saved_model_to_mlir(
    save_model_path, ','.join(exported_names), show_debug_info)
# We don't strictly need this, but it serves as a handy sanity check
# for that API, which is otherwise a bit annoying to test.
# The canonicalization shouldn't affect these tests in any way.
mlir = pywrap_mlir.experimental_run_pass_pipeline(mlir, 'canonicalize',
                                                  show_debug_info)
print(mlir)
filename = '%s/result.mlirbc' % save_model_path
pywrap_mlir.experimental_write_bytecode(filename, mlir)
if not file_io.file_exists(filename):
    raise app.UsageError('Failed to create bytecode output.')
