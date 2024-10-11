# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
if value < self.start or value == self.start and not self.start_included:
    exit(False)
if value > self.end or value == self.end and not self.end_included:
    exit(False)
exit(True)
