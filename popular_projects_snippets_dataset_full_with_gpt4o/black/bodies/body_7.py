# Extracted from ./data/repos/black/src/black/linegen.py
"""Generate a line.

        If the line is empty, only emit if it makes sense.
        If the line is too long, split it first and then generate.

        If any lines were generated, set up a new current_line.
        """
if not self.current_line:
    self.current_line.depth += indent
    exit()  # Line is empty, don't emit. Creating a new one unnecessary.

complete_line = self.current_line
self.current_line = Line(mode=self.mode, depth=complete_line.depth + indent)
exit(complete_line)
