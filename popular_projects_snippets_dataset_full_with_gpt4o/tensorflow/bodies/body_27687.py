# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
"""Test that all constraints are met for given parameters."""
if not is_batch_size_static:
    # Adding a constant value here prevents downstream computation from
    # statically deriving the value of global batch size when running
    # in graph mode.
    global_batch_size += constant_op.constant(0, dtypes.int64)

batch_sizes_list = []
for i in range(num_workers):
    batch_sizes_list.append(
        self.evaluate(
            distribute.batch_sizes_for_worker(global_batch_size, num_workers,
                                              num_replicas_per_worker, i)))
for batch_sizes in batch_sizes_list:
    # Constraint (A): for any worker, len(batch_sizes) == W * R
    self.assertLen(batch_sizes, num_workers * num_replicas_per_worker)
    # Constraint (B): for any worker, sum(batch_sizes) == G
    self.assertAllEqual(np.sum(batch_sizes), global_batch_size)

# Each per-worker batch is split into num_workers global steps
for step_index in range(num_workers):
    actual_global_batch = 0
    offset = step_index * num_replicas_per_worker
    for batch_sizes in batch_sizes_list:
        actual_global_batch += np.sum(batch_sizes[offset:offset +
                                                  num_replicas_per_worker])
    # Constraint (C): for any step, batch size across all workers add up to G.
    self.assertAllEqual(
        global_batch_size,
        actual_global_batch,
    )

# Constraint (D): Batch size of any two replicas differs by at most one
self.assertLessEqual(np.max(batch_sizes_list) - np.min(batch_sizes_list), 1)
