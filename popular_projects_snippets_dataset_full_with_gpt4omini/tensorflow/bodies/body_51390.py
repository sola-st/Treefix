# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
params = [
    dict(testcase_name="ReloadOncePy", cycles=1, use_cpp_bindings=False),
    dict(testcase_name="ReloadTwicePy", cycles=2, use_cpp_bindings=False),
    dict(testcase_name="ReloadThricePy", cycles=3, use_cpp_bindings=False),
]
if not run_external:
    params.append(dict(testcase_name="ReloadOnceCpp", cycles=1,
                       use_cpp_bindings=True))
exit(params)
