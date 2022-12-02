import pytest


class CustomDict:

    def __init__(self):
        self.data = {}
        self.counter = 0

    def __setitem__(self, key, value):
        if key not in self.data:
            self.counter += 1
        self.data[key] = value

    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            raise KeyError(key)

    def __delitem__(self, key):
        try:
            del self.data[key]
            self.counter -= 1
        except KeyError:
            raise KeyError(key)

    def __iter__(self):
        for k, v in self.data.items():
            yield k, v

    def __len__(self):
        return self.counter


dic = CustomDict()


def test_should_create_new_item():
    dic['a'] = 12
    assert len(dic) == 1


def test_should_get_item():
    assert dic['a'] == 12


def test_should_raise_error_not_exists():
    with pytest.raises(Exception):
        assert dic['b'] == 17


def test_should_update_item():
    dic['a'] = 18
    assert dic['a'] == 18
    assert len(dic) == 1


def test_should_del_item():
    del dic['a']
    assert len(dic) == 0
    with pytest.raises(Exception):
        assert dic['a']


def test_should_be_iterable():
    keys = ['a', 'b', 'c']
    values = [12, 7, 30]

    for k, v in zip(keys, values):
        dic[k] = v

    counter = 0
    for k, v in dic:
        assert k, v == list(zip(keys, values))[counter]
        counter += 1

    assert counter == 3
