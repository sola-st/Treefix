import pathlib # pragma: no cover
import re # pragma: no cover

root = pathlib.Path('/root/directory').absolute() # pragma: no cover
paths = [pathlib.Path('/root/directory/file1.py'), pathlib.Path('/root/directory/dir1')] # pragma: no cover
def normalize_path_maybe_ignore(path, root, report): return str(path.relative_to(root)) # pragma: no cover
report = type('Mock', (object,), {'path_ignored': lambda self, child, message: print(f'Ignored: {child} because {message}')})() # pragma: no cover
gitignore_dict = {root / pathlib.Path('.gitignore'): 'content'} # pragma: no cover
def path_is_ignored(path, gitignore_dict, report): return False # pragma: no cover
def path_is_excluded(path, regex): return bool(regex.search(path)) if regex else False # pragma: no cover
exclude = re.compile(r'exclude_regex') # pragma: no cover
extend_exclude = re.compile(r'extend_exclude_regex') # pragma: no cover
force_exclude = re.compile(r'force_exclude_regex') # pragma: no cover
def get_gitignore(path): return 'gitignore_content' # pragma: no cover
def gen_python_files(paths, root, include, exclude, extend_exclude, force_exclude, report, gitignore_dict, verbose, quiet): return 0 # pragma: no cover
include = re.compile(r'include_regex') # pragma: no cover
verbose = True # pragma: no cover
quiet = False # pragma: no cover
def jupyter_dependencies_are_installed(verbose, quiet): return True # pragma: no cover

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
_l_(18932)
for child in paths:
    _l_(18961)

    normalized_path = normalize_path_maybe_ignore(child, root, report)
    _l_(18933)
    if normalized_path is None:
        _l_(18935)

        continue
        _l_(18934)

    # First ignore files matching .gitignore, if passed
    if gitignore_dict and path_is_ignored(child, gitignore_dict, report):
        _l_(18937)

        continue
        _l_(18936)

    # Then ignore with `--exclude` `--extend-exclude` and `--force-exclude` options.
    normalized_path = "/" + normalized_path
    _l_(18938)
    if child.is_dir():
        _l_(18940)

        normalized_path += "/"
        _l_(18939)

    if path_is_excluded(normalized_path, exclude):
        _l_(18943)

        report.path_ignored(child, "matches the --exclude regular expression")
        _l_(18941)
        continue
        _l_(18942)

    if path_is_excluded(normalized_path, extend_exclude):
        _l_(18946)

        report.path_ignored(
            child, "matches the --extend-exclude regular expression"
        )
        _l_(18944)
        continue
        _l_(18945)

    if path_is_excluded(normalized_path, force_exclude):
        _l_(18949)

        report.path_ignored(child, "matches the --force-exclude regular expression")
        _l_(18947)
        continue
        _l_(18948)

    if child.is_dir():
        _l_(18960)

        # If gitignore is None, gitignore usage is disabled, while a Falsey
        # gitignore is when the directory doesn't have a .gitignore file.
        if gitignore_dict is not None:
            _l_(18952)

            new_gitignore_dict = {
                **gitignore_dict,
                root / child: get_gitignore(child),
            }
            _l_(18950)
        else:
            new_gitignore_dict = None
            _l_(18951)
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
        _l_(18953)
        exit(aux)

    elif child.is_file():
        _l_(18959)

        if child.suffix == ".ipynb" and not jupyter_dependencies_are_installed(
            verbose=verbose, quiet=quiet
        ):
            _l_(18955)

            continue
            _l_(18954)
        include_match = include.search(normalized_path) if include else True
        _l_(18956)
        if include_match:
            _l_(18958)

            aux = child
            _l_(18957)
            exit(aux)
