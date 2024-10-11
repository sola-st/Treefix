# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# If a model contains a layer loaded from SavedModel, and if the model is
# loaded under tf.distribute.Strategy, it can't be saved and loaded again
# under tf.distribute.Strategy.
#
# Although the error is the same models with TF2 SavedModel, the cause is
# different. TF1 models loaded in API contain an intializer, which is
# invoked upon loading. Since loading is in the cross-replica context, that
# fails.
#
# Note that these saved model can still be loaded and used without
# tf.distribute.Strategy.
#
# Some tf.hub layers are converted from TF1, by loading TF1 saved model in
# TF2 then saved in TF2. This issue disables them to work with
# tf.distribute.Strategy.
v1_export_dir = self.get_temp_dir()

with tf1.Graph().as_default(), tf1.Session() as sess:
    v = tf1.Variable(1., use_resource=True)
    sess.run(v.initializer)
    builder = tf1.saved_model.Builder(v1_export_dir)
    builder.add_meta_graph_and_variables(
        sess,
        tags=[tf1.saved_model.tag_constants.TRAINING],
        main_op=tf1.tables_initializer(),
        strip_default_attrs=True)
    builder.save()

v1_loaded = tf.saved_model.load(v1_export_dir)
v2_export_dir = self.get_temp_dir()
tf.saved_model.save(v1_loaded, v2_export_dir)
with strategy.scope():
    # TODO(b/150009657): remove after fix.
    # got error, want no error.
    with self.assertRaisesRegex(
        tf.errors.InvalidArgumentError,
        "from the cross-replica context in an in-replica context"):
        tf.saved_model.load(v2_export_dir)
