# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline_test.py
"""Tests that Timeline can handle RPC tracing."""
metadata = config_pb2.RunMetadata()
step_stats = metadata.step_stats
dev_stats = step_stats.dev_stats.add()
dev_stats.device = '/job:worker/replica:0/task:0/cpu:0'
node_stats = dev_stats.node_stats.add()
node_stats.node_name = 'RecvTensor'
node_stats.all_start_micros = 12345
node_stats.op_end_rel_micros = 42
node_stats.timeline_label = ('[1024B] edge_160_conv2/biases/read from '
                             '/job:ps/replica:0/task:3/cpu:0 to '
                             '/job:worker/replica:0/task:0/cpu:0')
tl = timeline.Timeline(step_stats)
ctf = tl.generate_chrome_trace_format()
self._validateTrace(ctf)
