# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/common_v1.py
"""Runs test.

  1. Performs absl and tf "main"-like initialization that must run before almost
     anything else.
  2. Converts signature_def_map to SavedModel V1
  3. Converts SavedModel V1 to MLIR
  4. Prints the textual MLIR to stdout (it is expected that the caller will have
     FileCheck checks in its file to check this output).

  This is only for use by the MLIR SavedModel importer tests.

  Args:
    create_signature: A functor that return signature_def_map, init_op and
      assets_collection. signature_def_map is a map from string key to
      signature_def. The key will be used as function name in the resulting
      MLIR.
    canonicalize: If true, canonicalizer will be run on the resulting MLIR.
    show_debug_info: If true, shows debug locations in the resulting MLIR.
    use_lite: If true, importer will not do any graph transformation such as
      lift variables.
    lift_variables: If false, no variable lifting will be done on the graph.
  """

# Make LOG(ERROR) in C++ code show up on the console.
# All `Status` passed around in the C++ API seem to eventually go into
# `LOG(ERROR)`, so this makes them print out by default.
logging.set_stderrthreshold('error')

def app_main(argv):
    """Function passed to absl.app.run."""
    if len(argv) > 1:
        raise app.UsageError('Too many command-line arguments.')
    if FLAGS.save_model_path:
        save_model_path = FLAGS.save_model_path
    else:
        save_model_path = tempfile.mktemp(suffix='.saved_model')

    signature_def_map, init_op, assets_collection = create_signature()

    sess = tf.Session()
    sess.run(tf.initializers.global_variables())
    builder = tf.saved_model.builder.SavedModelBuilder(save_model_path)
    builder.add_meta_graph_and_variables(
        sess, [tf.saved_model.tag_constants.SERVING],
        signature_def_map,
        main_op=init_op,
        assets_collection=assets_collection,
        strip_default_attrs=True)
    builder.save()

    logging.info('Saved model to: %s', save_model_path)
    exported_names = ''
    upgrade_legacy = True
    if use_lite:
        mlir = pywrap_mlir.experimental_convert_saved_model_v1_to_mlir_lite(
            save_model_path, exported_names,
            ','.join([tf.saved_model.tag_constants.SERVING]),
            upgrade_legacy, show_debug_info)
        # We don't strictly need this, but it serves as a handy sanity check
        # for that API, which is otherwise a bit annoying to test.
        # The canonicalization shouldn't affect these tests in any way.
        mlir = pywrap_mlir.experimental_run_pass_pipeline(mlir,
                                                          'tf-standard-pipeline',
                                                          show_debug_info)
    else:
        mlir = pywrap_mlir.experimental_convert_saved_model_v1_to_mlir(
            save_model_path, exported_names,
            ','.join([tf.saved_model.tag_constants.SERVING]),
            lift_variables, upgrade_legacy, show_debug_info)

    if canonicalize:
        mlir = pywrap_mlir.experimental_run_pass_pipeline(mlir, 'canonicalize',
                                                          show_debug_info)
    print(mlir)

app.run(app_main)
