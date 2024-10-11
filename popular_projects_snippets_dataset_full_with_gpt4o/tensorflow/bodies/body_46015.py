# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py
globs = {}
exec(code, globs)  # pylint:disable=exec-used
exit(globs[name])
