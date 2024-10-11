# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_hash_table_asset_v1.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

shutil.rmtree(FLAGS.saved_model_path)

variable_scope.enable_resource_variables()

# Create the graph
table_initializer = lookup_ops.TextFileInitializer(
    write_vocabulary_file(['cat', 'is', 'on', 'the', 'mat']), dtypes.string,
    lookup_ops.TextFileIndex.WHOLE_LINE, dtypes.int64,
    lookup_ops.TextFileIndex.LINE_NUMBER)
table = lookup_ops.StaticVocabularyTable(
    table_initializer, num_oov_buckets=10)

key = array_ops.placeholder(dtypes.string, shape=(), name='input')
result = table.lookup(key)

sess = session.Session()

sess.run(variables.global_variables_initializer())

sm_builder = builder.SavedModelBuilder(FLAGS.saved_model_path)
tensor_info_x = utils.build_tensor_info(key)
tensor_info_r = utils.build_tensor_info(result)

toy_signature = (
    signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name=signature_constants.PREDICT_METHOD_NAME))

sm_builder.add_meta_graph_and_variables(
    sess, [tag_constants.SERVING],
    signature_def_map={
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: toy_signature,
    },
    main_op=lookup_ops.tables_initializer(),
    assets_collection=ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS),
    strip_default_attrs=True)
sm_builder.save()
