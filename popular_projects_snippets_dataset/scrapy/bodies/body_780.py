# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
if opts.meta:
    try:
        opts.meta = json.loads(opts.meta)
    except ValueError:
        raise UsageError("Invalid -m/--meta value, pass a valid json string to -m or --meta. "
                         "Example: --meta='{\"foo\" : \"bar\"}'", print_help=False)
