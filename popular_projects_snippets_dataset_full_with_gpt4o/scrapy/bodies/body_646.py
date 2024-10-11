# Extracted from ./data/repos/scrapy/scrapy/utils/project.py
if ENVVAR not in os.environ:
    project = os.environ.get('SCRAPY_PROJECT', 'default')
    init_env(project)

settings = Settings()
settings_module_path = os.environ.get(ENVVAR)
if settings_module_path:
    settings.setmodule(settings_module_path, priority='project')

valid_envvars = {
    'CHECK',
    'PROJECT',
    'PYTHON_SHELL',
    'SETTINGS_MODULE',
}

scrapy_envvars = {k[7:]: v for k, v in os.environ.items() if
                  k.startswith('SCRAPY_') and k.replace('SCRAPY_', '') in valid_envvars}

settings.setdict(scrapy_envvars, priority='project')

exit(settings)
