# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
output_path = tempfile.mktemp()

ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 2 >> %s\n" % output_path),
        self._EXIT
    ])

ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(
    ["Syntax error for command: babble", "For help, do \"help babble\""],
    ui.unwrapped_outputs[0].lines)

# Clean up output file.
gfile.Remove(output_path)
