# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
with self.assertRaisesRegex(ValueError, "Invalid ui_type: 'foobar'"):
    ui_factory.get_ui(
        "foobar",
        config=cli_config.CLIConfig(config_file_path=self._tmp_config_path))
