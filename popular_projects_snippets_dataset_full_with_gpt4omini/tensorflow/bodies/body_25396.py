# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("mouse off\n"), string_to_codes("mouse on\n"),
        string_to_codes("babble\n"), self._EXIT
    ])
ui.register_command_handler("babble", self._babble, "")

ui.run_ui()
self.assertTrue(ui._mouse_enabled)
self.assertIn("Mouse: ON", ui.scroll_messages[-1])
