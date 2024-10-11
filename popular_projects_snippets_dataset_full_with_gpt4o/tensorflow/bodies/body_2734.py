# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
version = self.backend.platform_version
logging.info("platform_version:\n%s", version)
if self.backend.platform == "cpu":
    self.assertEqual(version, "<unknown>")
elif self.backend.platform == "gpu":
    # Following is false if not built with --config=cuda
    if version != "<unknown>":
        self.assertTrue(
            re.match(r"^cuda \d{4,}$", version),
            msg=f"Expected CUDA version string; got {repr(version)}")
elif self.backend.platform == "tpu" and not pathways:
    self.assertIn("tpu", version.lower())
    self.assertIn("cl/", version)
    self.assertIn("Built on ", version)
