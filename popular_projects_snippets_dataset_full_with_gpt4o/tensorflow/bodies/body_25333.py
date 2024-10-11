# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
# Omit non-ASCII key codes.
exit("".join(chr(code) for code in cmd_code if code < 256))
