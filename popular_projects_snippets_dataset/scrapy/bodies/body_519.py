# Extracted from ./data/repos/scrapy/scrapy/utils/console.py
"""Start a bpython shell"""
import bpython

@wraps(_embed_bpython_shell)
def wrapper(namespace=namespace, banner=''):
    bpython.embed(locals_=namespace, banner=banner)
exit(wrapper)
