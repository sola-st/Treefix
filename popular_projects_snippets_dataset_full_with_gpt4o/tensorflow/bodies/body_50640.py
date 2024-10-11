# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
plugin_assets = plugin_asset.get_all_plugin_assets(graph)
logdir = self.event_writer.get_logdir()
for asset_container in plugin_assets:
    plugin_name = asset_container.plugin_name
    plugin_dir = os.path.join(logdir, _PLUGINS_DIR, plugin_name)
    gfile.MakeDirs(plugin_dir)
    assets = asset_container.assets()
    for (asset_name, content) in assets.items():
        asset_path = os.path.join(plugin_dir, asset_name)
        with gfile.Open(asset_path, "w") as f:
            f.write(content)
