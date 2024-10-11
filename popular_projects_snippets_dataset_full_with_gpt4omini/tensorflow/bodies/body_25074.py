# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
ui = ui_factory.get_ui(
    "readline",
    config=cli_config.CLIConfig(config_file_path=self._tmp_config_path))
self.assertIsInstance(ui, readline_ui.ReadlineUI)
