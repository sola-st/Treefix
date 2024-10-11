import click # pragma: no cover

self = type('Mock', (object,), {'check': False, 'diff': False, 'change_count': 0, 'same_count': 0, 'failure_count': 0}) # pragma: no cover
style = lambda text, bold=False, fg=None: text # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/report.py
from l3.Runtime import _l_
"""Render a color report of the current state.

        Use `click.unstyle` to remove colors.
        """
if self.check or self.diff:
    _l_(15984)

    reformatted = "would be reformatted"
    _l_(15978)
    unchanged = "would be left unchanged"
    _l_(15979)
    failed = "would fail to reformat"
    _l_(15980)
else:
    reformatted = "reformatted"
    _l_(15981)
    unchanged = "left unchanged"
    _l_(15982)
    failed = "failed to reformat"
    _l_(15983)
report = []
_l_(15985)
if self.change_count:
    _l_(15988)

    s = "s" if self.change_count > 1 else ""
    _l_(15986)
    report.append(
        style(f"{self.change_count} file{s} ", bold=True, fg="blue")
        + style(f"{reformatted}", bold=True)
    )
    _l_(15987)

if self.same_count:
    _l_(15991)

    s = "s" if self.same_count > 1 else ""
    _l_(15989)
    report.append(style(f"{self.same_count} file{s} ", fg="blue") + unchanged)
    _l_(15990)
if self.failure_count:
    _l_(15994)

    s = "s" if self.failure_count > 1 else ""
    _l_(15992)
    report.append(style(f"{self.failure_count} file{s} {failed}", fg="red"))
    _l_(15993)
aux = ", ".join(report) + "."
_l_(15995)
exit(aux)
