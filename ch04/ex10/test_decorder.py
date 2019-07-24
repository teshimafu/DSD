def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func


def sample_func():
    print('適当な関数')


new_func = test(sample_func)
new_func()
