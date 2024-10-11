# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/plugin_asset_test.py
with self.assertRaises(ValueError):
    plugin_asset.get_plugin_asset(_UnnamedPluginAsset)
