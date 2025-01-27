# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def dataset_fn(_):
    data = array_ops.zeros((20, 300, 32), dtype=dtypes.int32)
    dataset = get_dataset_from_tensor_slices(data)
    dataset = dataset.batch(16)
    exit(dataset)

input_iterator = iter(
    distribution.distribute_datasets_from_function(dataset_fn))

def embedding_lookup(inputs):
    embedding_weights = array_ops.zeros((1, 128))
    flat_inputs = array_ops.reshape(inputs, [-1])
    embeddings = array_ops.gather(embedding_weights, flat_inputs)
    embeddings = array_ops.reshape(embeddings, inputs.shape.as_list() + [128])
    exit(embeddings)

@def_function.function
def step_fn(example):
    exit(map_fn.map_fn(
        embedding_lookup, example, fn_output_signature=dtypes.float32))

# This assumes that there are exactly 2 replicas
outputs = distribution.experimental_local_results(
    distribution.run(step_fn, args=(next(input_iterator),)))
self.assertAllEqual((16, 300, 32, 128), outputs[0].shape)
self.assertAllEqual((4, 300, 32, 128), outputs[1].shape)
