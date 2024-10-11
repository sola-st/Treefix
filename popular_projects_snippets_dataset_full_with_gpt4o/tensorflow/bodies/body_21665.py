# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(),
                              'evaluate_perfect_model_once')

# Train a Model to completion:
self._train_model(checkpoint_dir, num_steps=300)

# Run
inputs = constant_op.constant(self._inputs, dtype=dtypes.float32)
labels = constant_op.constant(self._labels, dtype=dtypes.float32)
logits = logistic_classifier(inputs)
predictions = math_ops.round(logits)

accuracy, update_op = metrics_module.accuracy(labels, predictions)

checkpoint_path = saver.latest_checkpoint(checkpoint_dir)

final_ops_values = evaluation._evaluate_once(
    checkpoint_path=checkpoint_path,
    eval_ops=update_op,
    final_ops={'accuracy': (accuracy, update_op)},
    hooks=[
        evaluation._StopAfterNEvalsHook(1),
    ])
self.assertGreater(final_ops_values['accuracy'], .99)
