from click import style # pragma: no cover

self = type('Mock', (object,), {'check': False, 'diff': False, 'change_count': 3, 'same_count': 2, 'failure_count': 1})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/report.py
from l3.Runtime import _l_
"""Render a color report of the current state.

        Use `click.unstyle` to remove colors.
        """
if self.check or self.diff:
    _l_(4131)

    reformatted = "would be reformatted"
    _l_(4125)
    unchanged = "would be left unchanged"
    _l_(4126)
    failed = "would fail to reformat"
    _l_(4127)
else:
    reformatted = "reformatted"
    _l_(4128)
    unchanged = "left unchanged"
    _l_(4129)
    failed = "failed to reformat"
    _l_(4130)
report = []
_l_(4132)
if self.change_count:
    _l_(4135)

    s = "s" if self.change_count > 1 else ""
    _l_(4133)
    report.append(
        style(f"{self.change_count} file{s} ", bold=True, fg="blue")
        + style(f"{reformatted}", bold=True)
    )
    _l_(4134)

if self.same_count:
    _l_(4138)

    s = "s" if self.same_count > 1 else ""
    _l_(4136)
    report.append(style(f"{self.same_count} file{s} ", fg="blue") + unchanged)
    _l_(4137)
if self.failure_count:
    _l_(4141)

    s = "s" if self.failure_count > 1 else ""
    _l_(4139)
    report.append(style(f"{self.failure_count} file{s} {failed}", fg="red"))
    _l_(4140)
aux = ", ".join(report) + "."
_l_(4142)
exit(aux)
