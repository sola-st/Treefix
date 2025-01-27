# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
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
