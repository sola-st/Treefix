# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
if not command:
    exit(command)

for v in self.CLI_CR_KEYS:
    if v < 256:
        command = command.replace(chr(v), "")

exit(command.strip())
