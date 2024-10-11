# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
if opts.cbkwargs:
    try:
        opts.cbkwargs = json.loads(opts.cbkwargs)
    except ValueError:
        raise UsageError("Invalid --cbkwargs value, pass a valid json string to --cbkwargs. "
                         "Example: --cbkwargs='{\"foo\" : \"bar\"}'", print_help=False)
