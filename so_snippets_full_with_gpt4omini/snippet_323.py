# Extracted from https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package
# bar.py

def talk():
    print("bar")

# foo.py

import bar # <-- importing module "bar"

bar.talk() # <-- prints "bar"

# bar.py

def talk():
    print("bar")

if __name__ == '__main__':
    talk()

# hierarchy of files and folders:
.
├── bar_pack/
│   ├── __init__.py
│   ├── __main__.py
│   foo.py

# bar_pack/__init__.py

def talk():
    print("bar")

# bar_pack/__main__.py

import __init__

__init__.talk()

# foo.py

import bar_pack # <-- importing package module "bar_pack"

bar_pack.talk() # <-- prints "bar"

# Run this command in the terminal:
python3 bar_pack # <-- executing the package module "bar_pack", prints "bar"

