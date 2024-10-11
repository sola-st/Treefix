# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
raise NotImplementedError(f"ON_READ variables doesn't support `{method}` "
                          "in cross replica context")
