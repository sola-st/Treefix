# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/abs_fuzz.py
atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
atheris.Fuzz()
