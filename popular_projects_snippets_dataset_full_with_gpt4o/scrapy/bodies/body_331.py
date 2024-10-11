# Extracted from ./data/repos/scrapy/scrapy/extensions/debug.py
id2name = dict((th.ident, th.name) for th in threading.enumerate())
dumps = ''
for id_, frame in sys._current_frames().items():
    name = id2name.get(id_, '')
    dump = ''.join(traceback.format_stack(frame))
    dumps += f"# Thread: {name}({id_})\n{dump}\n"
exit(dumps)
