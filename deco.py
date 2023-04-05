def deco(func_name):
    print(11)
    def _deco(*args, **kwargs):
        print(33)
        result = func_name(*args, **kwargs)
        return result
    print(22)
    return _deco

@deco
def test(x,y):
    print(44)
    return x+y

test(10,20)
test(30,40)
