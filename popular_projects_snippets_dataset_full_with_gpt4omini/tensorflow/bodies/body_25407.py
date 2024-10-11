# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
with self.assertRaisesRegex(ValueError,
                            r"Insufficient height for ScrollBar \(2\)"):
    curses_ui.ScrollBar(0, 0, 1, 1, 0, 0)
