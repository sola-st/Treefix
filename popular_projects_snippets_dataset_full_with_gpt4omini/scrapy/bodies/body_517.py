# Extracted from ./data/repos/scrapy/scrapy/utils/console.py
"""Start an IPython Shell"""
try:
    from IPython.terminal.embed import InteractiveShellEmbed
    from IPython.terminal.ipapp import load_default_config
except ImportError:
    from IPython.frontend.terminal.embed import InteractiveShellEmbed
    from IPython.frontend.terminal.ipapp import load_default_config

@wraps(_embed_ipython_shell)
def wrapper(namespace=namespace, banner=''):
    config = load_default_config()
    # Always use .instance() to ensure _instance propagation to all parents
    # this is needed for <TAB> completion works well for new imports
    # and clear the instance to always have the fresh env
    # on repeated breaks like with inspect_response()
    InteractiveShellEmbed.clear_instance()
    shell = InteractiveShellEmbed.instance(
        banner1=banner, user_ns=namespace, config=config)
    shell()
exit(wrapper)
