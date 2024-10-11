# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
try:
    MockCursesUI(40, 80)
except ValueError as e:
    result.put(e)
