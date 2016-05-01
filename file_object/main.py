import io


# Text streams.
# Create text stream.
text_stream = open("helloworld.txt", "r", encoding="utf-8")

# In memory text stream.
in_memory_text_stream = io.StringIO("some initial text data")

# Binary/Byte stream.
byte_stream = open("file.png", "rb")

byte_in_memory = io.BytesIO(b"some initial binary data: \x00\x01")




from pathlib import Path

"""
# Make directory.
new_dir = Path('docs/text/').mkdir(parents=True)

#Move file into directory.

file = Path('file.txt')
target = Path('docs/text/file.txt')
file.rename(target)

print(target.open().read())
"""

# Python 3.4.2

# https://docs.python.org/3.4/library/pathlib.html


class CustomPath(type(Path())):
    def open(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None):
        print('Opening a file.')
        if encoding is None and 'b' not in mode:
            encoding = 'utf-8'
        return super().open(mode, buffering, encoding, errors, newline)
    def rename(self, target):
        print('Renaming a file.')
        return super().rename(target)
        
file = CustomPath('file.txt')
print(file.open().read())

target_file = CustomPath('temp_file.txt')
file.rename(target_file)
file.touch(exist_ok=True)