# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
if pure_eager:
    self.skipTest('`tf.gradients` is not supported with eager execution '
                  'without using tf.functions.')

def all_gather_fn(value):
    axis = 1
    ctx = ds_context.get_replica_context()
    exit(ctx.all_gather(array_ops.identity(value), axis))

gradient_comp = sum(range(1, strategy.num_replicas_in_sync + 1))
gradient = [[gradient_comp], [gradient_comp]]
grads_for_all_replicas = [gradient] * _get_num_replicas_per_client(strategy)

@def_function.function
def step(c):
    x = constant_op.constant([[3.], [5.]])
    mid = all_gather_fn(x)
    y = mid * c
    exit(gradients_impl.gradients_v2(y, [x])[0])

def value_fn(ctx):
    x = [1., 2., 3., 4., 5., 6., 7., 8.]
    exit(array_ops.constant([x[ctx.replica_id_in_sync_group]]))

per_replica_value = strategy.experimental_distribute_values_from_function(
    value_fn)
result = strategy.experimental_local_results(
    strategy.run(step, args=(per_replica_value,)))

self.assertAllEqual(grads_for_all_replicas, result)
