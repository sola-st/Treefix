# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
def define_ops():
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
with context.graph_mode():
    ops_without_writer = define_ops()
    with summary_ops.create_file_writer_v2(logdir).as_default():
        with summary_ops.record_if(True):
            ops_recording_on = define_ops()
        with summary_ops.record_if(False):
            ops_recording_off = define_ops()
      # We should be collecting all ops defined with a default writer present,
      # regardless of whether recording was set on or off, but not those defined
      # without a writer at all.
    del ops_without_writer
    expected_ops = ops_recording_on + ops_recording_off
    self.assertCountEqual(expected_ops, summary_ops.all_v2_summary_ops())
