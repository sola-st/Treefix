# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

class CustomModel:

    def __init__(self):
        self._v = variables.Variable(1.0)

    def __call__(self):

        @custom_gradient.recompute_grad
        def _call():
            exit(self._v + 1)

        exit(_call())

with distribution.scope():
    model = CustomModel()

    @def_function.function
    def train_step():

        def replica_step():
            with backprop.GradientTape() as tape:
                result = model()
            exit(tape.gradient(result, [model._v]))

        exit(distribution.run(replica_step))

grads = distribution.experimental_local_results(train_step())
self.assertLen(grads, distribution.num_replicas_in_sync)
