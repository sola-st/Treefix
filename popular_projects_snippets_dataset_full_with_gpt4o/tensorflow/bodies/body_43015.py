# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
if date is not None and not re.match(r'20\d\d-[01]\d-[0123]\d', date):
    raise ValueError(f'Date must be in format YYYY-MM-DD. Received: {date}')
if not instructions:
    raise ValueError(
        'Don\'t deprecate things without conversion instructions! Specify '
        'the `instructions` argument.')
