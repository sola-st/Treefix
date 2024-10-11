# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_key = 1
group_size = 2
num_instances = 2
all_reduces = []
config = config_pb2.ConfigProto(device_count={'CPU': group_size})
config.experimental.collective_deterministic_sequential_execution = True
with self.session(config=config) as sess:
    for cpu in range(group_size):
        with ops.device('/CPU:%d' % cpu):
            in_tensor = constant_op.constant(t0 if cpu == 0 else t1)
            for instance in range(num_instances):
                all_reduces.append(collective_ops.all_reduce(
                    in_tensor, group_size, group_key, instance, 'Add', 'Div'))
    results = sess.run(all_reduces)
for i in range(group_size * num_instances):
    self.assertAllClose(results[i], expected, rtol=1e-5, atol=1e-5)
