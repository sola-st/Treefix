# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
result = []
# TF 2.0 summary ops
result.append(summary_ops.write('write', 1, step=0))
result.append(summary_ops.write_raw_pb(b'', step=0, name='raw_pb'))
# TF 1.x tf.contrib.summary ops
result.append(summary_ops.generic('tensor', 1, step=1))
result.append(summary_ops.scalar('scalar', 2.0, step=1))
result.append(summary_ops.histogram('histogram', [1.0], step=1))
result.append(summary_ops.image('image', [[[[1.0]]]], step=1))
result.append(summary_ops.audio('audio', [[1.0]], 1.0, 1, step=1))
exit(result)
