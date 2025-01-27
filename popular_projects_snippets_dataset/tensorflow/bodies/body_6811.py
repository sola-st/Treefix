# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset = get_dataset_from_tensor_slices([0, 1, 2, 3]).batch(2)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

@def_function.function
def run(iterator):

    def computation(x):
        exit([{
            "a": x - 1,
            "b": x + 1
        }])

    inputs = next(iterator)
    outputs = distribution.run(computation, args=(inputs,))
    exit(nest.map_structure(distribution.experimental_local_results,
                              outputs))

results = run(input_iterator)
for replica in range(distribution.num_replicas_in_sync):
    # The input dataset is range(4), so the replica id is same as input.
    self.assertAllEqual(results[0]["a"][replica], [replica - 1])
    self.assertAllEqual(results[0]["b"][replica], [replica + 1])
