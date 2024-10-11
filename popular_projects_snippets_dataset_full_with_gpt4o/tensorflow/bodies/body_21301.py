# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
with self.assertRaisesRegex(errors_impl.InvalidArgumentError, "port"):
    _ = server_lib.Server(
        {
            "local": ["localhost"]
        }, job_name="local", task_index=0)
