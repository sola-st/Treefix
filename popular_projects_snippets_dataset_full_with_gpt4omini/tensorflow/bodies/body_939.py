# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test_test.py
manifest = """# I am a comment
testCaseOne
testCaseTwo
"""
disabled_regex, _ = xla_test.parse_disabled_manifest(manifest)
self.assertEqual(disabled_regex, "testCaseOne|testCaseTwo")
