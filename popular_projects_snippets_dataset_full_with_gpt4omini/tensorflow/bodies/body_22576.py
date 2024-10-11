# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
with ops.Graph().as_default():
    training_util.create_global_step()
    read_tensor = training_util._get_or_create_global_step_read()
    inc_op = training_util._increment_global_step(1)
    inc_three_op = training_util._increment_global_step(3)
    with monitored_session.MonitoredTrainingSession() as sess:
        read_value, _ = sess.run([read_tensor, inc_op])
        self.assertEqual(0, read_value)
        read_value, _ = sess.run([read_tensor, inc_three_op])
        self.assertEqual(1, read_value)
        read_value = sess.run(read_tensor)
        self.assertEqual(4, read_value)
