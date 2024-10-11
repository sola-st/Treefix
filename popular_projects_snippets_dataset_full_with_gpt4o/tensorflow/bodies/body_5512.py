# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
if context.executing_eagerly():
    run_options = None
else:
    # TODO(b/151025792): figure out why missing run options would make the
    # test flaky and whether this is a problem in TF 2.
    run_options = config_pb2.RunOptions()
    run_options.experimental.collective_graph_key = 5
super(CollectiveAllReduceTest, self)._assert_mirrored_equal(
    left_list, right_list, sess, run_options=run_options)
