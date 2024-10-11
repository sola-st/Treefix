# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/save_restore_ops_test.py
with session.Session(
    target="", config=config_pb2.ConfigProto(device_count={"CPU": 2})):
    self.assertEqual(
        gen_io_ops.sharded_filename("foo", 4, 100).eval(),
        b"foo-00004-of-00100")
    self.assertEqual(
        gen_io_ops.sharded_filespec("foo", 100).eval(), b"foo-?????-of-00100")
