# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
model = self._create_trackable()
input_value = constant_op.constant([[3.]])
expected_output = self.evaluate(model(input_value))
model.deferred_variable = variables_lib.Variable(5.)

checkpoint = trackable_utils.Checkpoint(model)
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
save_path = checkpoint.save(checkpoint_prefix)

new_model = self._create_trackable()
load_checkpoint = trackable_utils.Checkpoint(new_model)
load_checkpoint.restore(save_path)
self.assertAllClose(expected_output, new_model(input_value))

new_model.deferred_variable = variables_lib.Variable(1.)
self.assertEqual(self.evaluate(new_model.deferred_variable), 5)
