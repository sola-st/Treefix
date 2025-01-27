# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def dataset_fn(_):
    data = array_ops.zeros((5, 1, 2), dtype=dtypes.int32)
    dataset = get_dataset_from_tensor_slices(data)
    dataset = dataset.batch(3)
    exit(dataset)

input_iterator = iter(
    distribution.distribute_datasets_from_function(dataset_fn))

@def_function.function
def step_fn(example):
    # example: [<=3, 1, 2]
    # tile: [<=3, <=3, 2]
    tile = array_ops.tile(example, [1, array_ops.shape(example)[0], 1])
    # reshape1: [<=(3*3 = 9), 2]
    reshape1 = array_ops.reshape(tile, [-1, 2])

    # reshape2: [<=3, <=3, 2]
    reshape2 = array_ops.reshape(
        reshape1,
        [array_ops.shape(example)[0],
         array_ops.shape(example)[0], 2])

    # reshape3: [<=3, -1, 2]
    reshape3 = array_ops.reshape(reshape1,
                                 [array_ops.shape(example)[0], -1, 2])
    # reshape4: [-1, <=3, 2]
    reshape4 = array_ops.reshape(reshape1,
                                 [-1, array_ops.shape(example)[0], 2])
    # Reshape1 is duplicated in order to test dynamic dimension on copies.
    exit([reshape1, reshape2, reshape3, reshape4, reshape1])

# This assumes that there are exactly 2 replicas
outputs = distribution.experimental_local_results(
    distribution.run(step_fn, args=(next(input_iterator),)))
self.assertAllEqual((9, 2), outputs[0][0].shape)
self.assertAllEqual((3, 3, 2), outputs[0][1].shape)
self.assertAllEqual((3, 3, 2), outputs[0][2].shape)
self.assertAllEqual((3, 3, 2), outputs[0][3].shape)
self.assertAllEqual((9, 2), outputs[0][4].shape)

self.assertAllEqual((4, 2), outputs[1][0].shape)
self.assertAllEqual((2, 2, 2), outputs[1][1].shape)
self.assertAllEqual((2, 2, 2), outputs[1][2].shape)
self.assertAllEqual((2, 2, 2), outputs[1][3].shape)
self.assertAllEqual((4, 2), outputs[1][4].shape)
