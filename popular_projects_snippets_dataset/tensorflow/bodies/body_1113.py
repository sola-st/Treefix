# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
comments_re = re.compile('#.*$')
disabled_tests = []
disabled_method_types = []
for l in manifest_content.splitlines():
    stripped = comments_re.sub('', l).strip()
    if not stripped:
        continue
    entry = stripped.split(' ')
    if len(entry) == 1:
        disabled_tests.append(entry[0])
    elif len(entry) == 2:
        disabled_method_types.append((entry[0], entry[1].strip().split(',')))
    else:
        raise ValueError('Bad entry in manifest file.')

disabled_regex = '|'.join(disabled_tests)
method_types_filter = {}
for method, types in disabled_method_types:
    method_types_filter[method] = set([
        dtypes.as_dtype(types_pb2.DataType.Value(name)).as_numpy_dtype
        for name in types
    ])
exit((disabled_regex, method_types_filter))
