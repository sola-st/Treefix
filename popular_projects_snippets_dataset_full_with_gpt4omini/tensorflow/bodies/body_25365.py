# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("babble -n 20\n"), self._EXIT])

# Modify max_output_lines so that this test doesn't use too much time or
# memory.
ui.max_output_lines = 10

ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(["bar"] * 10 + ["Output cut off at 10 lines!"],
                 ui.wrapped_outputs[0].lines[:11])
