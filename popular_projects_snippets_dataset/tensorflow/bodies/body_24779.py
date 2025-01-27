# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
log_messages = []
def fake_logging_info(*args):
    log_messages.append(args)
with test.mock.patch.object(
    tf_logging, "info", side_effect=fake_logging_info):
    dumping_callback.enable_dump_debug_info(
        self.dump_root, tensor_debug_mode=tensor_debug_mode)
    self.assertLen(log_messages, 1)
    self.assertIn(self.dump_root, log_messages[0])
    self.assertIn(tensor_debug_mode, log_messages[0])
