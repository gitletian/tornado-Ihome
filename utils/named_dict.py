# coding: utf-8
# __author__: ""


class Struct(object):
    def __init__(self, d):
        self.__dict__ = d


def d2s(d):
    if isinstance(d, (list, tuple)):
        return list(map(d2s, d))

    elif not isinstance(d, dict):
        return d

    return Struct(dict((k, d2s(v)) for (k, v) in d.items()))


def s2d(obj):
    if isinstance(obj, (list, tuple)):
        return list(map(s2d, obj))

    elif not isinstance(obj, Struct):
        return obj

    return {k: s2d(v) for (k, v) in obj.__dict__.items()}

