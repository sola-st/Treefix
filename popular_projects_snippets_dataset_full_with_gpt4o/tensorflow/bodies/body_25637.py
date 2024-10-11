# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler(
    "noop", self._noop_handler, "", prefix_aliases=["n"])

# Clash with existing alias.
with self.assertRaisesRegex(ValueError,
                            "clashes with existing prefixes or aliases"):
    registry.register_command_handler(
        "cols", self._echo_screen_cols, "", prefix_aliases=["n"])

# The name clash should have prevent the handler from being registered.
self.assertFalse(registry.is_registered("cols"))

# Aliases can also clash with command prefixes.
with self.assertRaisesRegex(ValueError,
                            "clashes with existing prefixes or aliases"):
    registry.register_command_handler(
        "cols", self._echo_screen_cols, "", prefix_aliases=["noop"])

self.assertFalse(registry.is_registered("cols"))
