# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
is_quotes = '\'' * isinstance(value, str)
exit(is_quotes + str(value) + is_quotes)
