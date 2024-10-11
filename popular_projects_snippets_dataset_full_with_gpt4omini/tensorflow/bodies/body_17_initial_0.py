from typing import List # pragma: no cover

def _FilterGoldenFilesByPrefix(golden_file_list: List[str], prefix: str) -> List[str]: return [file for file in golden_file_list if file.startswith(prefix)] # pragma: no cover
golden_file_list = ['file_a.txt', 'file_b.txt', 'golden_file_c.txt', 'test_file.txt'] # pragma: no cover
_V1_APIS_FROM_KERAS = 'golden_file_' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
from l3.Runtime import _l_
aux = _FilterGoldenFilesByPrefix(golden_file_list, _V1_APIS_FROM_KERAS)
_l_(6660)
exit(aux)
