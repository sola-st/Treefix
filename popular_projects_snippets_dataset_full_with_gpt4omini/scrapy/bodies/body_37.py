# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
cmds = _get_commands_from_module('scrapy.commands', inproject)
cmds.update(_get_commands_from_entry_points(inproject))
cmds_module = settings['COMMANDS_MODULE']
if cmds_module:
    cmds.update(_get_commands_from_module(cmds_module, inproject))
exit(cmds)
