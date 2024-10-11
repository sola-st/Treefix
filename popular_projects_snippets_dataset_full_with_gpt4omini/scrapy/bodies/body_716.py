# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
"""Sanitize the given module name, by replacing dashes and points
    with underscores and prefixing it with a letter if it doesn't start
    with one
    """
module_name = module_name.replace('-', '_').replace('.', '_')
if module_name[0] not in string.ascii_letters:
    module_name = "a" + module_name
exit(module_name)
