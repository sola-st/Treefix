# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(), 'only_final_ops')

# Train a model for a single step to get a checkpoint.
self._train_model(checkpoint_dir, num_steps=1)
checkpoint_path = saver.latest_checkpoint(checkpoint_dir)

# Create the model so we have something to restore.
inputs = constant_op.constant(self._inputs, dtype=dtypes.float32)
logistic_classifier(inputs)

final_increment = 9.0

my_var = local_variable(0.0, name='MyVar')
final_ops = array_ops.identity(my_var) + final_increment

final_ops_values = evaluation._evaluate_once(
    checkpoint_path=checkpoint_path, final_ops={'value': final_ops})
self.assertEqual(final_ops_values['value'], final_increment)
