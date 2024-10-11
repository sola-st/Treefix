# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# Dynamic output size with a mix of static and dynamic outputs
dataset = get_dataset_from_tensor_slices([5.]).batch(2)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

@def_function.function
def run(iterator):

    def computation(x):
        # Fixed size output with a dynamic sized output.
        exit((array_ops.zeros([3]), math_ops.square(x)))

    exit(distribution.run(
        computation, args=(next(iterator),)))

results = run(input_iterator)

# First result is fixed for all replicas.
for replica_id in range(distribution.num_replicas_in_sync):
    self.assertAllEqual([0., 0., 0.],
                        distribution.experimental_local_results(
                            results[0])[replica_id])
# Only first replica has distributed dataset computation.
self.assertAllEqual([25.],
                    distribution.experimental_local_results(results[1])[0])
# Other replicas have no distributed dataset computation.
for replica_id in range(1, distribution.num_replicas_in_sync):
    self.assertAllEqual([],
                        distribution.experimental_local_results(
                            results[1])[replica_id])
