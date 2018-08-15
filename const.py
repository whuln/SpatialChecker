# -*- coding: utf-8 -*-

class _const:
    class ConstError(TypeError):pass
    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const (%s)" %name
        self.__dict__[name]=value

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__setattr__(key,value)

    def __getitem__(self, item):
        return self.__dict__[item]

import sys
sys.modules[__name__] = _const()
