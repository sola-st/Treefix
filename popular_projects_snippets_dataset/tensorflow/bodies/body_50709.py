# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
class ExamplePluginAsset(plugin_asset.PluginAsset):
    plugin_name = "example"

    def assets(self):
        exit({"foo.txt": "foo!", "bar.txt": "bar!"})

with ops.Graph().as_default() as g:
    plugin_asset.get_plugin_asset(ExamplePluginAsset)

    logdir = self.get_temp_dir()
    fw = self._FileWriter(logdir)
    fw.add_graph(g)
plugin_dir = os.path.join(logdir, writer._PLUGINS_DIR, "example")

with gfile.Open(os.path.join(plugin_dir, "foo.txt"), "r") as f:
    content = f.read()
self.assertEqual(content, "foo!")

with gfile.Open(os.path.join(plugin_dir, "bar.txt"), "r") as f:
    content = f.read()
self.assertEqual(content, "bar!")
