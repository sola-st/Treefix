# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(), 'eval_ops_and_final_ops')

# Train a model for a single step to get a checkpoint.
self._train_model(checkpoint_dir, num_steps=1)
checkpoint_path = saver.latest_checkpoint(checkpoint_dir)

# Create the model so we have something to restore.
inputs = constant_op.constant(self._inputs, dtype=dtypes.float32)
logistic_classifier(inputs)

num_evals = 6

my_var = local_variable(0.0, name='MyVar')
# In eval ops, we also increase the eval step one more time.
eval_ops = [state_ops.assign_add(my_var, 1.0),
            state_ops.assign_add(
                evaluation._get_or_create_eval_step(), 1, use_locking=True)]
expect_eval_update_counts = num_evals // 2

final_ops = array_ops.identity(my_var)

final_ops_values = evaluation._evaluate_once(
    checkpoint_path=checkpoint_path,
    eval_ops=eval_ops,
    final_ops={'value': final_ops},
    hooks=[evaluation._StopAfterNEvalsHook(num_evals),])
self.assertEqual(final_ops_values['value'], expect_eval_update_counts)
