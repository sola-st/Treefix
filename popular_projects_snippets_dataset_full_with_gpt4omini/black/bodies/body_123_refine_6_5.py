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
err = lambda message: sys.stderr.write(message + '\n') # pragma: no cover
class MockPathSpec:# pragma: no cover
    @staticmethod# pragma: no cover
    def from_lines(mode, lines):# pragma: no cover
        return f'PathSpec created with mode: {mode} and lines: {lines}' # pragma: no cover
class MockGitWildMatchPatternError(Exception):# pragma: no cover
    pass # pragma: no cover
GitWildMatchPatternError = MockGitWildMatchPatternError # pragma: no cover
PathSpec = MockPathSpec # pragma: no cover
lines = ['myenv*\n', '*.swp\n', '*~\n', 'iids*.json\n', 'trace_*.h5\n', '__pycache__\n', 'workspace.code-workspace\n', '*_instr.py\n', '/data\n', '/dist\n', '*.egg-info\n', '.vscode/launch.json\n', '*.orig\n', 'training_loss.csv\n', 'train*.pt\n', 'validate*.pt\n', 'all_training_traces.txt\n', 'checkpoint-last\n', 'functions_under_test\n', 'bodies_under_test\n', 'metrics*.csv\n', 'trace*.txt\n', 'build\n', 'eval_examples.pkl\n', 'validation_acc.csv\n', 'tests/test.py\n', '*.out\n', '*.log\n', 'popular_projects_snippets_dataset\n', 'tmp\n', 'pynguin-report\n', 'flask_files.txt\n', 'pyrightconfig.json\n', 'out*\n', 'so_snippets_dataset/*\n', '*_dataset.txt\n', 'files/subset*\n', 'metrics__*\n', 'temp.py\n', 'gpt_cache.json'] # pragma: no cover

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
