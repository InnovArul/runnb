from pkgutil import iter_modules


def module_exists(module_name):
    return module_name in (name for loader, name, ispkg in iter_modules())


def test_install():
    print("running test for runnb installation check")
    is_module_exists = module_exists("runnb")
    print(is_module_exists)
    assert is_module_exists, "module runnb not installed"

