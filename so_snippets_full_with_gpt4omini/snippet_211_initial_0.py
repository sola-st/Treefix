import os # pragma: no cover

CANDIDATE_BRANCH = 'feature-branch' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty
from l3.Runtime import _l_
os.system('powershell.exe  rmdir -r D:\workspace\Branches\*%s* -Force' %CANDIDATE_BRANCH)
_l_(1470)

