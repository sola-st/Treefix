# Extracted from https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
from shutil import make_archive
make_archive(
  'zipfile_name', 
  'zip',           # the archive format - or tar, bztar, gztar 
  root_dir=None,   # root for archive - current working dir if None
  base_dir=None)   # start archiving from here - cwd if None too

make_archive('zipfile_name', 'zip', root_dir='.')

python -m zipfile -c zipname sourcedir

python -m zipfile -c zipname sourcedir/*

python zipname

python -m zipapp myapp
python myapp.pyz

