# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
"""Generate the spider module, based on the given template"""
capitalized_module = ''.join(s.capitalize() for s in module.split('_'))
tvars = {
    'project_name': self.settings.get('BOT_NAME'),
    'ProjectName': string_camelcase(self.settings.get('BOT_NAME')),
    'module': module,
    'name': name,
    'domain': domain,
    'classname': f'{capitalized_module}Spider'
}
if self.settings.get('NEWSPIDER_MODULE'):
    spiders_module = import_module(self.settings['NEWSPIDER_MODULE'])
    spiders_dir = Path(spiders_module.__file__).parent.resolve()
else:
    spiders_module = None
    spiders_dir = Path(".")
spider_file = f"{spiders_dir / module}.py"
shutil.copyfile(template_file, spider_file)
render_templatefile(spider_file, **tvars)
print(f"Created spider {name!r} using template {template_name!r} ",
      end=('' if spiders_module else '\n'))
if spiders_module:
    print(f"in module:\n  {spiders_module.__name__}.{module}")
