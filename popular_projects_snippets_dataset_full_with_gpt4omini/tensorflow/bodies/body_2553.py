# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
computation = self.ExampleComputation()
executable = self.backend.compile(computation)
fingerprint = executable.fingerprint
if self.backend.platform == "tpu" and not (cloud_tpu or pathways):
    logging.info("fingerprint: %s", fingerprint)
    self.assertNotEmpty(fingerprint)
else:
    self.assertIsNone(fingerprint)
