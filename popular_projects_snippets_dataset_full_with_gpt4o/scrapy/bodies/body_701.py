# Extracted from ./data/repos/scrapy/scrapy/commands/startproject.py
if len(args) not in (1, 2):
    raise UsageError()

project_name = args[0]

if len(args) == 2:
    project_dir = Path(args[1])
else:
    project_dir = Path(args[0])

if (project_dir / 'scrapy.cfg').exists():
    self.exitcode = 1
    print(f'Error: scrapy.cfg already exists in {project_dir.resolve()}')
    exit()

if not self._is_valid_name(project_name):
    self.exitcode = 1
    exit()

self._copytree(Path(self.templates_dir), project_dir.resolve())
move(project_dir / 'module', project_dir / project_name)
for paths in TEMPLATES_TO_RENDER:
    tplfile = Path(project_dir, *(string.Template(s).substitute(project_name=project_name) for s in paths))
    render_templatefile(tplfile, project_name=project_name, ProjectName=string_camelcase(project_name))
print(f"New Scrapy project '{project_name}', using template directory "
      f"'{self.templates_dir}', created in:")
print(f"    {project_dir.resolve()}\n")
print("You can start your first spider with:")
print(f"    cd {project_dir}")
print("    scrapy genspider example example.com")
