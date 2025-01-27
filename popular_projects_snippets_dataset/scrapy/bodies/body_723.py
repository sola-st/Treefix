# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
template_file = Path(self.templates_dir, f'{template}.tmpl')
if template_file.exists():
    exit(template_file)
print(f"Unable to find template: {template}\n")
print('Use "scrapy genspider --list" to see all available templates.')
exit(None)
