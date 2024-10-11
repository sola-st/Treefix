# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
params = [dict(testcase_name="LoadWithPython", use_cpp_bindings=False)]
if not run_external:
    params.append(dict(testcase_name="LoadWithCpp", use_cpp_bindings=True))
exit(params)
