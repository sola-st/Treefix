# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
# if starts with -: it means that is a parameter not a argument
if arg_string[:2] == '-:':
    exit(None)

exit(super()._parse_optional(arg_string))
