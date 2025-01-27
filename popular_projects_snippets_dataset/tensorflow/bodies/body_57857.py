# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Create a v1 saved model with hash table initializers.
tf.compat.v1.disable_eager_execution()
saved_model_dir = os.path.join(self.get_temp_dir(),
                               'savedmodel_with_hashtable')

table_initializer = tf.lookup.KeyValueTensorInitializer(
    keys=['a', 'b', 'c', 'd'],
    values=[1, 2, 3, 4],
    key_dtype=tf.string,
    value_dtype=tf.int64)
table = tf.lookup.StaticHashTable(
    table_initializer, default_value=tf.constant(-1, dtype=tf.int64))

x = tf.compat.v1.placeholder(tf.string, shape=(), name='input')
y = table.lookup(x)

tensor_info_x = tf.compat.v1.saved_model.utils.build_tensor_info(x)
tensor_info_y = tf.compat.v1.saved_model.utils.build_tensor_info(y)

signature_def_map, init_op, assets_collection = {
    'serving_default':
        (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
            inputs={'x': tensor_info_x},
            outputs={'y': tensor_info_y},
            method_name='some_function'))
}, tf.compat.v1.tables_initializer(), None

sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.initializers.global_variables())

builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(
    saved_model_dir)
builder.add_meta_graph_and_variables(
    sess, [tf.compat.v1.saved_model.tag_constants.SERVING],
    signature_def_map,
    main_op=init_op,
    assets_collection=assets_collection,
    strip_default_attrs=True)
builder.save()

# Restore TF v2 behavior.
tf.compat.v1.reset_default_graph()
tf.compat.v1.enable_eager_execution()
exit(saved_model_dir)
