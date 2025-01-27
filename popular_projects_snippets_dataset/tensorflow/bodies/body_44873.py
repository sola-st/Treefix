# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter.py
exit(parser.parse_expression('({})'.format(', '.join(
    'ag__.{}'.format(str(v)) for v in values))))
