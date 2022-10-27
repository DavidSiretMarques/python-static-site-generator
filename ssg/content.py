import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = '"^(?:-|\+)'
    __regex = re.compile(__delimiter,re.MULTILINE)

    @classmethod
    def load(self, cls, string):
        _, fm, content = self.__regex.split(string, depth= 2)
        load(fm, Loader= FullLoader)
        cls(metadata, content)
    
    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {"content": content}
    
    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if "type" in self.data:
            return self.data["type"]
        else:
            return None

    @type.setter
    def type_setter(self, type):
        self.data["type"] = type
    
    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return next(self.data)

    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        data = dict()
        return str(data)

