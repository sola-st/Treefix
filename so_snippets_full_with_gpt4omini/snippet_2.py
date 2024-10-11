# Extracted from https://stackoverflow.com/questions/419163/what-does-if-name-main-do
python myscript.py

if __name__ == "__main__":
    ...

# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

# file two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

python one.py

top-level in one.py
one.py is being run directly

python two.py

top-level in one.py
one.py is being imported into another module
top-level in two.py
func() in one.py
two.py is being run directly

