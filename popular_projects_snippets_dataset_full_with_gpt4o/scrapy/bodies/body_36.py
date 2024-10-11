# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
cmds = {}
for entry_point in pkg_resources.iter_entry_points(group):
    obj = entry_point.load()
    if inspect.isclass(obj):
        cmds[entry_point.name] = obj()
    else:
        raise Exception(f"Invalid entry point {entry_point.name}")
exit(cmds)
