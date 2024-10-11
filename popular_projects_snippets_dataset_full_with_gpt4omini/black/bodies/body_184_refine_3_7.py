from pathlib import Path # pragma: no cover
from typing import Set, Optional, Dict # pragma: no cover
import re # pragma: no cover

ctx = type('MockContext', (), {'obj': {'root': Path('/mock/root')}})() # pragma: no cover
exclude = None # pragma: no cover
DEFAULT_EXCLUDES = [] # pragma: no cover
src = ['/mock/src/file1.py', '/mock/src/file2.py', '-'] # pragma: no cover
stdin_filename = '/mock/stdin/file'  # pragma: no cover
report = type('MockReport', (), {'path_ignored': lambda self, p, msg: print(f'Ignored {p}: {msg}')})() # pragma: no cover
force_exclude = None # pragma: no cover
STDIN_PLACEHOLDER = 'stdin_' # pragma: no cover
verbose = True # pragma: no cover
quiet = False # pragma: no cover
include = [] # pragma: no cover
extend_exclude = [] # pragma: no cover
def re_compile_maybe_verbose(excludes): return re.compile('|'.join(excludes)) # pragma: no cover
def get_gitignore(path): return None # pragma: no cover
def normalize_path_maybe_ignore(p, root, report): return str(p.relative_to(root)) if p.exists() else None # pragma: no cover
def jupyter_dependencies_are_installed(verbose, quiet): return True # pragma: no cover
def gen_python_files(iterable, root, include, exclude, extend_exclude, force_exclude, report, gitignore, verbose, quiet): return set() # pragma: no cover
force_exclude = type('MockRegex', (), {'search': lambda self, path: None})() # pragma: no cover

from pathlib import Path # pragma: no cover
from typing import Set, Optional, Dict # pragma: no cover
import re # pragma: no cover

ctx = type('MockContext', (), {'obj': {'root': Path('/mock/root')}})() # pragma: no cover
exclude = None # pragma: no cover
DEFAULT_EXCLUDES = [] # pragma: no cover
src = ['/mock/src/file1.py', '/mock/src/file2.py', '-'] # pragma: no cover
stdin_filename = '/mock/stdin/file' # pragma: no cover
report = type('MockReport', (), {'path_ignored': lambda self, p, msg: print(f'Ignored {p}: {msg}')})() # pragma: no cover
force_exclude = None # pragma: no cover
STDIN_PLACEHOLDER = 'stdin_' # pragma: no cover
verbose = True # pragma: no cover
quiet = False # pragma: no cover
include = [] # pragma: no cover
extend_exclude = [] # pragma: no cover
def re_compile_maybe_verbose(excludes): return re.compile('|'.join(excludes)) # pragma: no cover
def get_gitignore(path): return None # pragma: no cover
def normalize_path_maybe_ignore(p, root, report): return str(p.relative_to(root)) if p.exists() else None # pragma: no cover
def jupyter_dependencies_are_installed(verbose, quiet): return True # pragma: no cover
def gen_python_files(iterable, root, include, exclude, extend_exclude, force_exclude, report, gitignore, verbose, quiet): return set() # pragma: no cover
PathSpec = type('MockPathSpec', (), {}) # pragma: no cover
gitignore = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Compute the set of files to be formatted."""
sources: Set[Path] = set()
_l_(7257)
root = ctx.obj["root"]
_l_(7258)

using_default_exclude = exclude is None
_l_(7259)
exclude = re_compile_maybe_verbose(DEFAULT_EXCLUDES) if exclude is None else exclude
_l_(7260)
gitignore: Optional[Dict[Path, PathSpec]] = None
_l_(7261)
root_gitignore = get_gitignore(root)
_l_(7262)

for s in src:
    _l_(7292)

    if s == "-" and stdin_filename:
        _l_(7267)

        p = Path(stdin_filename)
        _l_(7263)
        is_stdin = True
        _l_(7264)
    else:
        p = Path(s)
        _l_(7265)
        is_stdin = False
        _l_(7266)

    if is_stdin or p.is_file():
        _l_(7291)

        normalized_path = normalize_path_maybe_ignore(p, ctx.obj["root"], report)
        _l_(7268)
        if normalized_path is None:
            _l_(7270)

            continue
            _l_(7269)

        normalized_path = "/" + normalized_path
        _l_(7271)
        # Hard-exclude any files that matches the `--force-exclude` regex.
        if force_exclude:
            _l_(7274)

            force_exclude_match = force_exclude.search(normalized_path)
            _l_(7272)
        else:
            force_exclude_match = None
            _l_(7273)
        if force_exclude_match and force_exclude_match.group(0):
            _l_(7277)

            report.path_ignored(p, "matches the --force-exclude regular expression")
            _l_(7275)
            continue
            _l_(7276)

        if is_stdin:
            _l_(7279)

            p = Path(f"{STDIN_PLACEHOLDER}{str(p)}")
            _l_(7278)

        if p.suffix == ".ipynb" and not jupyter_dependencies_are_installed(
            verbose=verbose, quiet=quiet
        ):
            _l_(7281)

            continue
            _l_(7280)

        sources.add(p)
        _l_(7282)
    elif p.is_dir():
        _l_(7290)

        p = root / normalize_path_maybe_ignore(p, ctx.obj["root"], report)
        _l_(7283)
        if using_default_exclude:
            _l_(7285)

            gitignore = {
                root: root_gitignore,
                p: get_gitignore(p),
            }
            _l_(7284)
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
        _l_(7286)
    elif s == "-":
        _l_(7289)

        sources.add(p)
        _l_(7287)
    else:
        err(f"invalid path: {s}")
        _l_(7288)
aux = sources
_l_(7293)
exit(aux)
