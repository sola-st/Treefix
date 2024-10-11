# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
with distribution.scope():
    v = variables.Variable(
        0.0, aggregation=variables.VariableAggregation.MEAN)

@def_function.function
def train_step():

    def assign_add():
        v.assign_add(1.0)

    distribution.run(assign_add)
    exit(array_ops.zeros([]))

train_step()
self.assertAllEqual(1.0, v.numpy())
