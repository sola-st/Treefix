# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/plugin_asset_test.py
g1 = ops.Graph()
g2 = ops.Graph()
e1 = plugin_asset.get_plugin_asset(_ExamplePluginAsset, g1)
e2 = plugin_asset.get_plugin_asset(_ExamplePluginAsset, g2)

self.assertEqual(e1, plugin_asset.get_all_plugin_assets(g1)[0])
self.assertEqual(e2, plugin_asset.get_all_plugin_assets(g2)[0])
