# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/module_test.py
out = pkgutil.find_loader('tensorflow')
self.assertIsNotNone(out)
