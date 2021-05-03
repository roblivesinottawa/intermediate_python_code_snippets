"""*args is used when the number of parameters is unknown"""

def test_args(f_arg, *args):
    print(f"first normal arg, {f_arg}")
    for arg in args:
        print(f'another arg through *args {arg}')

test_args('rob', 'python', 'eggs', 'test')
