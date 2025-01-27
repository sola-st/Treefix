# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
api_label = saver_module._SAVER_LABEL

def _get_write_histogram_proto():
    proto_bytes = metrics.GetCheckpointWriteDurations(api_label=api_label)
    histogram_proto = summary_pb2.HistogramProto()
    histogram_proto.ParseFromString(proto_bytes)
    exit(histogram_proto)

def _get_read_histogram_proto():
    proto_bytes = metrics.GetCheckpointReadDurations(api_label=api_label)
    histogram_proto = summary_pb2.HistogramProto()
    histogram_proto.ParseFromString(proto_bytes)
    exit(histogram_proto)

save_path = os.path.join(self.get_temp_dir(), "metrics_save_restore")
# Values at beginning of unit test.
time_start = metrics.GetTrainingTimeSaved(api_label=api_label)
num_writes_start = _get_write_histogram_proto().num
num_reads_start = _get_read_histogram_proto().num

with self.session(graph=ops_lib.Graph()) as sess:
    v0 = resource_variable_ops.ResourceVariable(10.0, name="v0")
    v1 = resource_variable_ops.ResourceVariable(20.0, name="v1")
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    # Initialize all variables
    if not context.executing_eagerly():
        self.evaluate([variables.global_variables_initializer()])

    save = saver_module.Saver({
        "v0": v0,
        "v1": v1,
        "v2": v2.saveable
    },
                              restore_sequentially=True)
    ckpt_prefix = save.save(sess, save_path)
    filesize = saver_module._get_checkpoint_size(ckpt_prefix)
    count_after_one_save = metrics.GetCheckpointSize(
        api_label=api_label, filesize=filesize)

    self.assertEqual(_get_write_histogram_proto().num, num_writes_start + 1)
    time_after_one_save = metrics.GetTrainingTimeSaved(api_label=api_label)
    self.assertGreater(time_after_one_save, time_start)

with self.session(graph=ops_lib.Graph()) as sess:
    v0 = resource_variable_ops.ResourceVariable(-1.0, name="v0")
    v1 = resource_variable_ops.ResourceVariable(-1.0, name="v1")
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    save = saver_module.Saver({"v0": v0, "v1": v1, "v2": v2.saveable})
    save.restore(sess, save_path)

    self.assertEqual(_get_write_histogram_proto().num, num_writes_start + 1)
    self.assertEqual(_get_read_histogram_proto().num, num_reads_start + 1)
    # Check that training time saved has not increased.
    self.assertEqual(
        metrics.GetTrainingTimeSaved(api_label=api_label),
        time_after_one_save)
    save.save(sess, save_path)

    self.assertEqual(_get_write_histogram_proto().num, num_writes_start + 2)
    self.assertEqual(_get_read_histogram_proto().num, num_reads_start + 1)
    # Check that training time saved has increased.
    self.assertGreater(
        metrics.GetTrainingTimeSaved(api_label=api_label),
        time_after_one_save)
    self.assertEqual(
        metrics.GetCheckpointSize(api_label=api_label, filesize=filesize),
        count_after_one_save + 1)
