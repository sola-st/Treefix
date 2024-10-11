# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(), 'eval_ops_and_final_ops')

# Train a model for a single step to get a checkpoint.
self._train_model(checkpoint_dir, num_steps=1)
checkpoint_path = saver.latest_checkpoint(checkpoint_dir)

# Create the model so we have something to restore.
inputs = constant_op.constant(self._inputs, dtype=dtypes.float32)
logistic_classifier(inputs)

num_evals = 5
final_increment = 9.0

my_var = local_variable(0.0, name='MyVar')
eval_ops = state_ops.assign_add(my_var, 1.0)
final_ops = array_ops.identity(my_var) + final_increment

final_hooks = [evaluation._StopAfterNEvalsHook(num_evals),]
initial_hooks = list(final_hooks)
final_ops_values = evaluation._evaluate_once(
    checkpoint_path=checkpoint_path,
    eval_ops=eval_ops,
    final_ops={'value': final_ops},
    hooks=final_hooks)
self.assertEqual(final_ops_values['value'], num_evals + final_increment)
self.assertEqual(initial_hooks, final_hooks)
