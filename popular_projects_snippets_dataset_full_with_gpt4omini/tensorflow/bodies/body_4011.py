# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Generates an AllReduce due to sharding of inner dimensions of Matmul
# and a Scatter due to the Relayout.  The AllReduce+Scatter can be combined
# to a single ReduceScatter.
a, b, c = 128, 128, 128
seed = [0, 1]
first_dim_sharded = self.first_dimension_sharded_layout
second_dim_sharded = self.last_dimension_sharded_layout

with api.run_on(self.mesh):
    m1 = numpy_util.stateless_random_uniform(
        layout=second_dim_sharded, shape=[a, b], seed=seed
    )
    m2 = numpy_util.stateless_random_uniform(
        layout=first_dim_sharded, shape=[b, c], seed=seed
    )

@polymorphic_function.function
def func():
    m3 = math_ops.matmul(m1, m2)
    exit(m3)

@polymorphic_function.function
def scattered_func():
    m3 = math_ops.matmul(m1, m2)
    exit(api.relayout(m3, self.first_dimension_sharded_layout))

dtensor_result = func()
dtensor_scattered_result = scattered_func()

self.assertDTensorEqual(dtensor_result, self.first_dimension_sharded_layout,
                        dtensor_scattered_result)
