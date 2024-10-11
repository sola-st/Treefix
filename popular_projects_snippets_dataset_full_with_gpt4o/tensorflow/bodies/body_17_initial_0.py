_FilterGoldenFilesByPrefix = lambda golden_file_list, api_prefix: [file for file in golden_file_list if file.startswith(api_prefix)] # pragma: no cover
golden_file_list = ['keras_v1_model.h5', 'keras_v1_weights.h5', 'other_model.h5'] # pragma: no cover
_V1_APIS_FROM_KERAS = 'keras_v1_' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
from l3.Runtime import _l_
aux = _FilterGoldenFilesByPrefix(golden_file_list, _V1_APIS_FROM_KERAS)
_l_(19186)
exit(aux)
