"""this is used to pass keyworded arguments"""

def join(**kwargs):
    outcome = ""
    for arg in kwargs.values():
        outcome += arg
    return outcome

print(join(a="United", b="States", c="Of", d="America"))