# Extracted from ./data/repos/scrapy/scrapy/utils/console.py
"""Start a ptpython shell"""
import ptpython.repl

@wraps(_embed_ptpython_shell)
def wrapper(namespace=namespace, banner=''):
    print(banner)
    ptpython.repl.embed(locals=namespace)
exit(wrapper)
