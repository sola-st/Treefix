# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
mock_module = self.MockModule(name)
sys.modules[name] = mock_module
self._modules.append(name)
exit(mock_module)
