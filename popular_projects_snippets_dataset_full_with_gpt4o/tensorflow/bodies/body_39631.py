# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
first = trackable_utils.Checkpoint()
first.var1 = variables_lib.Variable(0., name="outside_var")
first.var2 = variables_lib.Variable(0., name="blah")
self.evaluate(first.var1.assign(4.))
self.evaluate(first.var2.assign(8.))
save_path = first.save(checkpoint_prefix)

second = trackable_utils.Checkpoint()
second.var2 = variables_lib.Variable(0., name="blah")
status = second.restore(save_path)
recreated_var1 = variables_lib.Variable(0., name="outside_var")
status.run_restore_ops()
self.assertEqual(8., self.evaluate(second.var2))
self.evaluate(recreated_var1.assign(-2.))
self.assertEqual(-2., self.evaluate(recreated_var1))
second.var1 = recreated_var1
status.run_restore_ops()
self.assertEqual(4., self.evaluate(recreated_var1))
