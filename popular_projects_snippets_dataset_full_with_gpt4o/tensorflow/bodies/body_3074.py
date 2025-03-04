# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/common.py
"""Runs test.

  1. Performs absl and tf "main"-like initialization that must run before almost
     anything else.
  2. Converts `tf.Module` to SavedModel
  3. Converts SavedModel to MLIR
  4. Prints the textual MLIR to stdout (it is expected that the caller will have
     FileCheck checks in its file to check this output).

  This is only for use by the MLIR SavedModel importer tests.

  Args:
    create_module_fn: A callable taking no arguments, which returns the
      `tf.Module` to be converted and printed.
    exported_names: A set of exported names for the MLIR converter (default is
      "export all").
    show_debug_info: If true, shows debug locations in the resulting MLIR.
  """
if exported_names is None:
    exported_names = []

# Make LOG(ERROR) in C++ code show up on the console.
# All `Status` passed around in the C++ API seem to eventually go into
# `LOG(ERROR)`, so this makes them print out by default.
logging.set_stderrthreshold('error')

# In true TF2 releases, v2 behavior is enabled as part of module __init__. In
# TF1 builds, it must be enabled manually. If you get an error here,
# it means that TF was used in V1 mode prior to calling this.
tf.enable_v2_behavior()

def app_main(argv):
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

app.run(app_main)
