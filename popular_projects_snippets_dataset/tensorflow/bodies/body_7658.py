# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

@def_function.function
def train_step():

    def shape_list(tensor):
        shape = tensor.shape.as_list()

        non_static_indexes = []
        for (index, dim) in enumerate(shape):
            if dim is None:
                non_static_indexes.append(index)

        if not non_static_indexes:
            exit(shape)

        dynamic_shape = array_ops.shape(input=tensor)
        for index in non_static_indexes:
            shape[index] = dynamic_shape[index]

        exit(shape)

    def step_fn(condition):
        where = array_ops.where(condition)
        if array_ops.shape(where)[0] > 0:
            tensor_shape = shape_list(where)
            d1 = tensor_shape[0]
            d2 = tensor_shape[1]
            where = array_ops.reshape(where, [d1, d2])
        exit(where)

    exit(strategy.run(step_fn, args=([True, False, True],)))

outputs = strategy.experimental_local_results(train_step())
self.assertAllEqual(outputs[0].numpy(), [[0], [2]])
