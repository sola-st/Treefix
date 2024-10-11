from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover
import sys # pragma: no cover

root = Path('.') # pragma: no cover
err = lambda message: sys.stderr.write(message + '\n') # pragma: no cover
class MockPathSpec:  # Mocking PathSpec for demonstration# pragma: no cover
    @staticmethod# pragma: no cover
    def from_lines(mode, lines):# pragma: no cover
        return 'PathSpec created with mode: ' + mode + ' and lines: ' + str(lines)# pragma: no cover
# pragma: no cover
PathSpec = MockPathSpec # pragma: no cover
class MockGitWildMatchPatternError(Exception):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
GitWildMatchPatternError = MockGitWildMatchPatternError # pragma: no cover

from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover
import sys # pragma: no cover

root = Path('.') # pragma: no cover
lines = [# pragma: no cover
    'myenv*\n',# pragma: no cover
    '*.swp\n',# pragma: no cover
    '*~\n',# pragma: no cover
    'iids*.json\n',# pragma: no cover
    'trace_*.h5\n',# pragma: no cover
    '__pycache__\n',# pragma: no cover
    'workspace.code-workspace\n',# pragma: no cover
    '*_instr.py\n',# pragma: no cover
    '/data\n',# pragma: no cover
    '/dist\n',# pragma: no cover
    '*.egg-info\n',# pragma: no cover
    '.vscode/launch.json\n',# pragma: no cover
    '*.orig\n',# pragma: no cover
    'training_loss.csv\n',# pragma: no cover
    'train*.pt\n',# pragma: no cover
    'validate*.pt\n',# pragma: no cover
    'all_training_traces.txt\n',# pragma: no cover
    'checkpoint-last\n',# pragma: no cover
    'functions_under_test\n',# pragma: no cover
    'bodies_under_test\n',# pragma: no cover
    'metrics*.csv\n',# pragma: no cover
    'trace*.txt\n',# pragma: no cover
    'build\n',# pragma: no cover
    'eval_examples.pkl\n',# pragma: no cover
    'validation_acc.csv\n',# pragma: no cover
    'tests/test.py\n',# pragma: no cover
    '*.out\n',# pragma: no cover
    '*.log\n',# pragma: no cover
    'popular_projects_snippets_dataset\n',# pragma: no cover
    'tmp\n',# pragma: no cover
    'pynguin-report\n',# pragma: no cover
    'flask_files.txt\n',# pragma: no cover
    'pyrightconfig.json\n',# pragma: no cover
    'out*\n',# pragma: no cover
    'so_snippets_dataset/*\n',# pragma: no cover
    '*_dataset.txt\n',# pragma: no cover
    'files/subset*\n',# pragma: no cover
    'metrics__*\n',# pragma: no cover
    'temp.py\n',# pragma: no cover
    'gpt_cache.json\n'# pragma: no cover
] # pragma: no cover
class MockPathSpec:  # Mocking PathSpec for demonstration# pragma: no cover
    @staticmethod# pragma: no cover
    def from_lines(mode, lines):# pragma: no cover
        return f'PathSpec created with mode: {mode} and lines: {lines}'# pragma: no cover
# pragma: no cover
PathSpec = MockPathSpec # pragma: no cover
class MockGitWildMatchPatternError(Exception):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
GitWildMatchPatternError = MockGitWildMatchPatternError # pragma: no cover
err = lambda message: print(f'Error: {message}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/files.py
from l3.Runtime import _l_
"""Return a PathSpec matching gitignore content if present."""
gitignore = root / ".gitignore"
_l_(3835)
lines: List[str] = []
_l_(3836)
if gitignore.is_file():
    _l_(3839)

    with gitignore.open(encoding="utf-8") as gf:
        _l_(3838)

        lines = gf.readlines()
        _l_(3837)
try:
    _l_(3844)

    aux = PathSpec.from_lines("gitwildmatch", lines)
    _l_(3840)
    exit(aux)
except GitWildMatchPatternError as e:
    _l_(3843)

    err(f"Could not parse {gitignore}: {e}")
    _l_(3841)
    raise
    _l_(3842)
