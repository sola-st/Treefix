# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
"""Randomly generates input/output data for a single test case.

    This function returns numpy constants for use in a test case.

    Args:
      num_classes: An int. The number of embedding classes in the test case.
      dim: An int. The dimension of the embedding.
      batch_size: An int. The batch size.
      num_true: An int. The number of target classes per training example.
      labels: A list of batch_size * num_true ints. The target classes.
      sampled: A list of indices in [0, num_classes).
      subtract_log_q: A bool corresponding to the parameter in
        _compute_sampled_logits().

    Returns:
      weights: Embedding weights to use as test input. It is a numpy array
          of shape [num_classes, dim]
      biases: Embedding biases to use as test input. It is a numpy array
          of shape [num_classes].
      hidden_acts: Forward activations of the network to use as test input.
          It is a numpy array of shape [batch_size, dim].
      sampled_vals: A tuple based on `sampled` to use as test input in the
          format returned by a *_candidate_sampler function.
      exp_logits: The output logits expected from _compute_sampled_logits().
          It is a numpy array of shape [batch_size, num_true + len(sampled)].
      exp_labels: The output labels expected from _compute_sampled_logits().
          It is a numpy array of shape [batch_size, num_true + len(sampled)].
    """
weights = np.random.randn(num_classes, dim).astype(np.float32)
biases = np.random.randn(num_classes).astype(np.float32)
hidden_acts = np.random.randn(batch_size, dim).astype(np.float32)

true_exp = np.full([batch_size, 1], fill_value=0.5, dtype=np.float32)
sampled_exp = np.full([len(sampled)], fill_value=0.5, dtype=np.float32)
sampled_vals = (sampled, true_exp, sampled_exp)

sampled_w, sampled_b = weights[sampled], biases[sampled]
true_w, true_b = weights[labels], biases[labels]

true_logits = np.sum(
    hidden_acts.reshape((batch_size, 1, dim)) * true_w.reshape(
        (batch_size, num_true, dim)),
    axis=2)
true_b = true_b.reshape((batch_size, num_true))
true_logits += true_b
sampled_logits = np.dot(hidden_acts, sampled_w.T) + sampled_b

if subtract_log_q:
    true_logits -= np.log(true_exp)
    sampled_logits -= np.log(sampled_exp[np.newaxis, :])

exp_logits = np.concatenate([true_logits, sampled_logits], axis=1)
exp_labels = np.hstack(
    (np.ones_like(true_logits) / num_true, np.zeros_like(sampled_logits)))

exit((weights, biases, hidden_acts, sampled_vals, exp_logits, exp_labels))
