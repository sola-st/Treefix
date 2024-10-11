# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(),
                              'evaluate_with_finite_inputs')

# Train a Model to completion:
self._train_model(checkpoint_dir, num_steps=300)

# Run evaluation. Inputs are fed through input producer for one epoch.
all_inputs = constant_op.constant(self._inputs, dtype=dtypes.float32)
all_labels = constant_op.constant(self._labels, dtype=dtypes.float32)

single_input, single_label = training.slice_input_producer(
    [all_inputs, all_labels], num_epochs=1)
inputs, labels = training.batch([single_input, single_label], batch_size=6,
                                allow_smaller_final_batch=True)

logits = logistic_classifier(inputs)
predictions = math_ops.round(logits)

accuracy, update_op = metrics_module.accuracy(labels, predictions)

checkpoint_path = saver.latest_checkpoint(checkpoint_dir)

final_ops_values = evaluation._evaluate_once(
    checkpoint_path=checkpoint_path,
    eval_ops=update_op,
    final_ops={
        'accuracy': (accuracy, update_op),
        'eval_steps': evaluation._get_or_create_eval_step()
    },
    hooks=[
        evaluation._StopAfterNEvalsHook(None),
    ])
self.assertTrue(final_ops_values['accuracy'] > .99)
# Runs evaluation for 4 iterations. First 2 evaluate full batch of 6 inputs
# each; the 3rd iter evaluates the remaining 4 inputs, and the last one
# triggers an error which stops evaluation.
self.assertEqual(final_ops_values['eval_steps'], 4)
