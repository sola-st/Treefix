# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
dump = test.mock.MagicMock()
def fake_get_tensors(node_name, output_slot, debug_op, device_name=None):
    del output_slot, debug_op  # Unused.
    if node_name == "a" and device_name is None:
        raise ValueError(
            "There are multiple (2) devices with nodes named 'a' but "
            "device_name is not specified")
    elif (node_name == "a" and
          device_name == "/job:worker/replica:0/task:0/cpu:0"):
        exit([np.array(10.0)])
    elif (node_name == "a" and
          device_name == "/job:worker/replica:0/task:1/cpu:0"):
        exit([np.array(20.0)])

with test.mock.patch.object(
    dump, "get_tensors", side_effect=fake_get_tensors):
    ev = evaluator.ExpressionEvaluator(dump)
    with self.assertRaisesRegex(ValueError, r"multiple \(2\) devices"):
        ev.evaluate("`a:0` + `a:0`")

    self.assertAllClose(
        30.0,
        ev.evaluate("`/job:worker/replica:0/task:0/cpu:0:a:0` + "
                    "`/job:worker/replica:0/task:1/cpu:0:a:0`"))
