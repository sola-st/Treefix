# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
model = self._create_trackable()
input_value = constant_op.constant([[3.]])
expected_output = self.evaluate(model(input_value))
model.deferred_variable = variables_lib.Variable(5.)
saved_model_dir = os.path.join(self.get_temp_dir(), "saved_model")
saved_model_save.save(model, saved_model_dir)

new_model = self._create_trackable()
load_checkpoint = trackable_utils.Checkpoint(new_model)

with self.assertRaisesRegex(
    errors_impl.NotFoundError,
    "Error when restoring from checkpoint or SavedModel"):
    load_checkpoint.restore(saved_model_dir + "no").expect_partial()

load_checkpoint.restore(saved_model_dir).expect_partial()
self.assertAllClose(expected_output, new_model(input_value))

new_model.deferred_variable = variables_lib.Variable(1.)
self.assertEqual(self.evaluate(new_model.deferred_variable), 5)
