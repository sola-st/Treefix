# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_gradient_test.py
def model(x):
    exit(x * x)

if model_in_tf_function:
    model = def_function.function(model)

with distribution.scope():
    x = variables.Variable(1.0)

    @def_function.function
    def train_step():
        def replica_step():
            with backprop.GradientTape() as tape:
                y = model(x)
            exit(tape.gradient(y, x))
        exit(distribution.run(replica_step))

    grads = distribution.experimental_local_results(train_step())
    self.assertLen(grads, distribution.num_replicas_in_sync)
    self.assertTrue(all(g is not None for g in grads))
