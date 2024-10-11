from typing import Set, Optional, Dict # pragma: no cover
from pathlib import Path # pragma: no cover
import re # pragma: no cover
import sys # pragma: no cover
from pathspec import PathSpec # pragma: no cover

ctx = type('Mock', (object,), {'obj': {'root': Path('/mock/root')}})() # pragma: no cover
src = ['/mock/root/existing_dir'] # pragma: no cover
exclude = None # pragma: no cover
DEFAULT_EXCLUDES = '.*' # pragma: no cover
re_compile_maybe_verbose = lambda pattern: re.compile(pattern) # pragma: no cover
get_gitignore = lambda path: PathSpec.from_lines('gitwildmatch', ['*.pyc', '__pycache__/']) # pragma: no cover
normalize_path_maybe_ignore = lambda p, root, report: str(p.relative_to(root)) if p.exists() else None # pragma: no cover
gen_python_files = lambda it, root, include, exclude, extend_exclude, force_exclude, report, gitignore, verbose, quiet: [Path(f'some_file_{i}.py') for i in range(5)] # pragma: no cover
stdin_filename = None # pragma: no cover
jupyter_dependencies_are_installed = lambda verbose, quiet: False # pragma: no cover
verbose = True # pragma: no cover
quiet = False # pragma: no cover
class Report:# pragma: no cover
    def path_ignored(self, path, reason):# pragma: no cover
        print(f"Path ignored: {path}, Reason: {reason}") # pragma: no cover
report = Report() # pragma: no cover
force_exclude = re.compile('.*') # pragma: no cover
include = None # pragma: no cover
extend_exclude = None # pragma: no cover
STDIN_PLACEHOLDER = '<stdin>' # pragma: no cover
def err(message):# pragma: no cover
    print(f"Error: {message}", file=sys.stderr) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Compute the set of files to be formatted."""
sources: Set[Path] = set()
_l_(19206)
root = ctx.obj["root"]
_l_(19207)

using_default_exclude = exclude is None
_l_(19208)
exclude = re_compile_maybe_verbose(DEFAULT_EXCLUDES) if exclude is None else exclude
_l_(19209)
gitignore: Optional[Dict[Path, PathSpec]] = None
_l_(19210)
root_gitignore = get_gitignore(root)
_l_(19211)

for s in src:
    _l_(19241)

    if s == "-" and stdin_filename:
        _l_(19216)

        p = Path(stdin_filename)
        _l_(19212)
        is_stdin = True
        _l_(19213)
    else:
        p = Path(s)
        _l_(19214)
        is_stdin = False
        _l_(19215)

    if is_stdin or p.is_file():
        _l_(19240)

        normalized_path = normalize_path_maybe_ignore(p, ctx.obj["root"], report)
        _l_(19217)
        if normalized_path is None:
            _l_(19219)

            continue
            _l_(19218)

        normalized_path = "/" + normalized_path
        _l_(19220)
        # Hard-exclude any files that matches the `--force-exclude` regex.
        if force_exclude:
            _l_(19223)

            force_exclude_match = force_exclude.search(normalized_path)
            _l_(19221)
        else:
            force_exclude_match = None
            _l_(19222)
        if force_exclude_match and force_exclude_match.group(0):
            _l_(19226)

            report.path_ignored(p, "matches the --force-exclude regular expression")
            _l_(19224)
            continue
            _l_(19225)

        if is_stdin:
            _l_(19228)

            p = Path(f"{STDIN_PLACEHOLDER}{str(p)}")
            _l_(19227)

        if p.suffix == ".ipynb" and not jupyter_dependencies_are_installed(
            verbose=verbose, quiet=quiet
        ):
            _l_(19230)

            continue
            _l_(19229)

        sources.add(p)
        _l_(19231)
    elif p.is_dir():
        _l_(19239)

        p = root / normalize_path_maybe_ignore(p, ctx.obj["root"], report)
        _l_(19232)
        if using_default_exclude:
            _l_(19234)

            gitignore = {
                root: root_gitignore,
                p: get_gitignore(p),
            }
            _l_(19233)
        sources.update(
            gen_python_files(
                p.iterdir(),
                ctx.obj["root"],
                include,
                exclude,
                extend_exclude,
                force_exclude,
                report,
                gitignore,
                verbose=verbose,
                quiet=quiet,
            )
        )
        _l_(19235)
    elif s == "-":
        _l_(19238)

        sources.add(p)
        _l_(19236)
    else:
        err(f"invalid path: {s}")
        _l_(19237)
aux = sources
_l_(19242)
exit(aux)
