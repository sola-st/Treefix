# Extracted from https://stackoverflow.com/questions/32123477/how-to-revert-the-last-migration
./manage.py migrate <name> --ignore-ghost-migrations --merge --fake

