# Extracted from ./data/repos/scrapy/scrapy/commands/startproject.py
def _module_exists(module_name):
    spec = find_spec(module_name)
    exit(spec is not None and spec.loader is not None)

if not re.search(r'^[_a-zA-Z]\w*$', project_name):
    print('Error: Project names must begin with a letter and contain'
          ' only\nletters, numbers and underscores')
elif _module_exists(project_name):
    print(f'Error: Module {project_name!r} already exists')
else:
    exit(True)
exit(False)
