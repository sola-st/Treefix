# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(1.0, name="v_one", trainable=False)
root.v2 = variables.Variable(2.0, name="v_two", trainable=True)
root.f = def_function.function(
    lambda x: root.v2 * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)],
)

if cycles > 1:
    root = cycle(root, cycles - 1, use_cpp_bindings=use_cpp_bindings)
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
save.save(root, path)

with ops.Graph().as_default() as g:
    imported = test_load(path, use_cpp_bindings=use_cpp_bindings)
    var_v1 = imported.v1
    self.assertFalse(var_v1.trainable)
    var_v2 = imported.v2
    self.assertTrue(var_v2.trainable)
    output = imported.f(constant_op.constant(2.0))
    with monitored_session.MonitoredSession() as sess:
        self.assertEqual(1.0, sess.run(var_v1))
        self.assertEqual(4.0, sess.run(output))
    self.assertCountEqual(
        [var_v1, var_v2], g.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    )
    # load() should not add to TRAINABLE_VARIABLES. Higher levels of model
    # building control retraining or frozen use of imported SavedModels.
    self.assertCountEqual(
        [], g.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    )
