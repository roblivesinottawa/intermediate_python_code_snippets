"""*args is used when the number of parameters is unknown"""

# def test_args(f_arg, *args):
#     print(f"first normal arg, {f_arg}")
#     for arg in args:
#         print(f'another arg through *args {arg}')
#
# test_args('rob', 'python', 'eggs', 'test')


def _sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(_sum(5,4,3,2,1))
