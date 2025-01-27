# Extracted from https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
   for mod in sys.modules.values():
      reload(mod)

