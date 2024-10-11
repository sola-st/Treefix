# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
attr = getattr(rewrite_options, option)
if attr != 0:
    options[option] = (attr == rewriter_config_pb2.RewriterConfig.ON)
