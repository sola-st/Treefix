# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/common_v1.py
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
