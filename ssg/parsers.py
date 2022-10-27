from typing import List
from pathlib import Path
import shutil

class Parser():
    def __init__(self):
        self.extensions = List[str]

    def valid_extension(self,extension):
        if extension in self.extensions:
            return True
        return False
    def parse(self, path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)
        raise NotImplementedError
    
    def read(self, path, dest, content):
        with open(path, 'r') as file:
            return file.read()

    def write(self, path, dest, content, ext = '.html'):
        full_path = self.dest / path.with_suffix(ext)
        with open(full_path, 'w') as file:
            return file.write(content)
    
    def copy(self, path, source, dest):
        shutil.copy2(path, dest/path.relative_to(source))



class ResourceParser(Parser):
    
    def __init__(self):
        self.extensions = [".jpg",".png",".gif",".css",".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
        