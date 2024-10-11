# Extracted from ./data/repos/black/src/black/report.py
"""Increment the counter for successful reformatting. Write out a message."""
if changed is Changed.YES:
    reformatted = "would reformat" if self.check or self.diff else "reformatted"
    if self.verbose or not self.quiet:
        out(f"{reformatted} {src}")
    self.change_count += 1
else:
    if self.verbose:
        if changed is Changed.NO:
            msg = f"{src} already well formatted, good job."
        else:
            msg = f"{src} wasn't modified on disk since last run."
        out(msg, bold=False)
    self.same_count += 1
