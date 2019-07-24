class OopsException(Exception):
    pass


try:
    raise OopsException()
except OopsException as exc:
    print('Caught an oops')
