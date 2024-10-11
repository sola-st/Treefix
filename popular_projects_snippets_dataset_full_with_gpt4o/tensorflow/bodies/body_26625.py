# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
config = server_lib.DispatcherConfig(fault_tolerant_mode=True)
error = "Cannot enable fault tolerant mode without configuring a work dir"
with self.assertRaisesRegex(ValueError, error):
    dispatcher = server_lib.DispatchServer(  # pylint: disable=unused-variable
        config=config, start=True)
