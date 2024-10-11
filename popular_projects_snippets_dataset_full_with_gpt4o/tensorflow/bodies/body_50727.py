# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/plugin_asset_test.py
plugin_asset.get_plugin_asset(_ExamplePluginAsset)
with self.assertRaises(ValueError):
    plugin_asset.get_plugin_asset(_ExamplePluginThatWillCauseCollision)
