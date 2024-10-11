# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/plugin_asset_test.py
epa = plugin_asset.get_plugin_asset(_ExamplePluginAsset)
self.assertIsInstance(epa, _ExamplePluginAsset)
epa2 = plugin_asset.get_plugin_asset(_ExamplePluginAsset)
self.assertIs(epa, epa2)
opa = plugin_asset.get_plugin_asset(_OtherExampleAsset)
self.assertIsNot(epa, opa)
