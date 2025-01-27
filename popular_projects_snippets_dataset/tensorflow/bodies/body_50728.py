# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/plugin_asset_test.py
epa = plugin_asset.get_plugin_asset(_ExamplePluginAsset)
opa = plugin_asset.get_plugin_asset(_OtherExampleAsset)
self.assertItemsEqual(plugin_asset.get_all_plugin_assets(), [epa, opa])
