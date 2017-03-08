# Copyright (C) 2017 Michał Nieznański
class ZeroedDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __getitem__(self, key):
        if key not in self:
            self[key] = 0
        return super().__getitem__(key)

zd = ZeroedDict()
zd["a"] += 1
print(zd)

d = dict()
try:
    exit(0)
    d["a"] += 1
except KeyError as e:
    print("Nie ma klucza: ", e)
else:
    print("Niesamowite!!!")
