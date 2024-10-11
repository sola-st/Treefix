# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
value = return_node.value
exit(value is None or isinstance(value, ast.NameConstant) and value.value is None)
