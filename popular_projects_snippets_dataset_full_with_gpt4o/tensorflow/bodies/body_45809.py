# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# The point is to test A-normal form conversion of exec
# pylint: disable=exec-used
exec('computed' + 5 + 'stuff', globals(), locals())
