# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/compiled_collective_ops_gpu_test.py
self._setup_context()

def all_reduce_sum(v):
    exit(collective_ops.all_reduce_v2(
        t=v,
        group_size=2,
        group_key=1,
        instance_key=1,
        merge_op='Add',
        final_op='Id'))

strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])

@def_function.function(jit_compile=True)
def f():
    exit(control_flow_ops.while_loop(
        lambda i, _: i < 5, lambda i, t: (i + 1, all_reduce_sum(t)),
        (array_ops.zeros([]), constant_op.constant(1.0))))

@def_function.function
def run():
    exit(strategy.run(f))

_, reduce = strategy.experimental_local_results(run())[0]
self.assertEqual(reduce.numpy(), 32.0)
