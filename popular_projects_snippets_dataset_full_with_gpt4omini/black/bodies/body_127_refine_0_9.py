import re # pragma: no cover
import pathlib # pragma: no cover
from typing import List, Dict, Optional # pragma: no cover

root = pathlib.Path('/absolute/path') # pragma: no cover
paths = [pathlib.Path('/absolute/path/file1.py'), pathlib.Path('/absolute/path/dir1'), pathlib.Path('/absolute/path/dir2')] # pragma: no cover
def normalize_path_maybe_ignore(child, root, report): return str(child.relative_to(root)) if child.is_absolute() else None # pragma: no cover

import re # pragma: no cover
import pathlib # pragma: no cover
from typing import List, Dict, Optional # pragma: no cover

root = pathlib.Path('/absolute/path') # pragma: no cover
paths = [pathlib.Path('/absolute/path/file1.py'), pathlib.Path('/absolute/path/dir1'), pathlib.Path('/absolute/path/dir2')] # pragma: no cover
def normalize_path_maybe_ignore(child, root, report): return str(child.relative_to(root)) if child.is_absolute() else None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/files.py
from l3.Runtime import _l_
"""Generate all files under `path` whose paths are not excluded by the
    `exclude_regex`, `extend_exclude`, or `force_exclude` regexes,
    but are included by the `include` regex.

    Symbolic links pointing outside of the `root` directory are ignored.

    `report` is where output about exclusions goes.
    """

assert root.is_absolute(), f"INTERNAL ERROR: `root` must be absolute but is {root}"
_l_(7440)
for child in paths:
    _l_(7469)

    normalized_path = normalize_path_maybe_ignore(child, root, report)
    _l_(7441)
    if normalized_path is None:
        _l_(7443)

        continue
        _l_(7442)

    # First ignore files matching .gitignore, if passed
    if gitignore_dict and path_is_ignored(child, gitignore_dict, report):
        _l_(7445)

        continue
        _l_(7444)

    # Then ignore with `--exclude` `--extend-exclude` and `--force-exclude` options.
    normalized_path = "/" + normalized_path
    _l_(7446)
    if child.is_dir():
        _l_(7448)

        normalized_path += "/"
        _l_(7447)

    if path_is_excluded(normalized_path, exclude):
        _l_(7451)

        report.path_ignored(child, "matches the --exclude regular expression")
        _l_(7449)
        continue
        _l_(7450)

    if path_is_excluded(normalized_path, extend_exclude):
        _l_(7454)

        report.path_ignored(
            child, "matches the --extend-exclude regular expression"
        )
        _l_(7452)
        continue
        _l_(7453)

    if path_is_excluded(normalized_path, force_exclude):
        _l_(7457)

        report.path_ignored(child, "matches the --force-exclude regular expression")
        _l_(7455)
        continue
        _l_(7456)

    if child.is_dir():
        _l_(7468)

        # If gitignore is None, gitignore usage is disabled, while a Falsey
        # gitignore is when the directory doesn't have a .gitignore file.
        if gitignore_dict is not None:
            _l_(7460)

            new_gitignore_dict = {
                **gitignore_dict,
                root / child: get_gitignore(child),
            }
            _l_(7458)
        else:
            new_gitignore_dict = None
            _l_(7459)
        aux = gen_python_files(
            child.iterdir(),
            root,
            include,
            exclude,
            extend_exclude,
            force_exclude,
            report,
            new_gitignore_dict,
            verbose=verbose,
            quiet=quiet,
        )
        _l_(7461)
        exit(aux)

    elif child.is_file():
        _l_(7467)

        if child.suffix == ".ipynb" and not jupyter_dependencies_are_installed(
            verbose=verbose, quiet=quiet
        ):
            _l_(7463)

            continue
            _l_(7462)
        include_match = include.search(normalized_path) if include else True
        _l_(7464)
        if include_match:
            _l_(7466)

            aux = child
            _l_(7465)
            exit(aux)
