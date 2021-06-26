import random

import pytest
import inspect
import re
import closures
import os
from closures import *

README_CONTENT_CHECK_FOR = [
    'doc_string_validator',
    'gen_next_fib_num',
    'fn_run_counter',
    'add',
    'mul',
    'div',
    'fn_run_counter_1',
    'fn_run_counter_2'
]


def function_name_has_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False


def test_function_names():
    assert not function_name_has_cap_letter(closures), "One of your function has a capitalized alphabet!"


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_proper_description():
    readme_looks_good = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            readme_looks_good = False
            pass
    assert readme_looks_good, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 40


def test_indentations():
    lines = inspect.getsource(closures)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def function_with_less_no_string():
    pass


def function_with_less_doc_string():
    """
    pass
    :return:
    """
    pass


def function_with_more_doc_string():
    """
    This is a sample function which contains more than fifty characters in its docstring
    :return: does not return anything
    """
    pass


def test_doc_string_validator_positive():
    validator = closures.doc_string_validator(function_with_more_doc_string)
    assert validator()


def test_doc_string_validator_negative():
    validator = closures.doc_string_validator(function_with_less_doc_string)
    assert not validator()


def test_doc_string_validator_none():
    validator = closures.doc_string_validator(function_with_less_doc_string)
    assert not validator()


def test_doc_string_validator_non_function():
    with pytest.raises(TypeError):
        var = 5
        validator = closures.doc_string_validator(var)
        validator()


def test_doc_string_validator_is_closure():
    validator = closures.doc_string_validator(function_with_less_doc_string)
    assert validator.__closure__


def test_gen_next_fib():
    fib = gen_next_fib_num()
    val = 0
    gen_fib = []
    for i in range(5):
        val = fib()
        gen_fib.append(val)
    assert val == 8
    assert gen_fib == [1, 2, 3, 5, 8]


def test_gen_next_fib_1():
    fib1 = gen_next_fib_num()
    fib2 = gen_next_fib_num()
    val1 = 0
    val2 = 0

    for i in range(5):
        val1 = fib1()
        val2 = fib2()

    assert val1 == val2


def test_gen_next_fib_is_closure():
    fib = gen_next_fib_num()
    assert fib.__closure__


def test_fn_run_counter_1_is_closure():
    fn = fn_run_counter_1(add)
    assert fn.__closure__


def test_fn_run_counter_1_add_count_pos():
    # clear dict as it would have been modified in above test cases
    fn_count_dict.clear()
    count_add = fn_run_counter_1(add)
    r = random.randint(1, 10)
    for i in range(r):
        count_add(random.random(), random.random())
    assert fn_count_dict['add'] == r


def test_fn_run_counter_1_mul_count_pos():
    # clear dict as it would have been modified in above test cases
    fn_count_dict.clear()
    count_mul = fn_run_counter_1(mul)
    r = random.randint(1, 10)
    for i in range(r):
        count_mul(random.random(), random.random())
    assert fn_count_dict['mul'] == r


def test_fn_run_counter_1_div_count_pos():
    # clear dict as it would have been modified in above test cases
    fn_count_dict.clear()
    count_div = fn_run_counter_1(div)
    r = random.randint(1, 10)
    for i in range(r):
        count_div(random.randint(1, 10), random.randint(1, 10))
    assert fn_count_dict['div'] == r


def test_fn_run_counter_1_add_count_neg():
    # clear dict as it would have been modified in above test cases
    fn_count_dict.clear()
    count_add = fn_run_counter_1(add)
    r = random.randint(1, 10)

    for i in range(r):
        count_add(random.random(), random.random())
    assert not fn_count_dict.get('mul') and not fn_count_dict.get('div')


def test_fn_run_counter_1_count_all():
    count_add = fn_run_counter_1(add)
    count_mul = fn_run_counter_1(mul)
    count_div = fn_run_counter_1(div)
    # clear dict as it would have been modified in above test cases
    fn_count_dict.clear()
    r1 = random.randint(1, 10)
    for i in range(r1):
        count_add(random.random(), random.random())
    assert fn_count_dict['add'] == r1

    r2 = random.randint(1, 10)
    for i in range(r2):
        count_mul(random.random(), random.random())
    assert fn_count_dict['mul'] == r2

    r3 = random.randint(1, 10)
    for i in range(r3):
        count_div(random.randint(1, 10), random.randint(1, 10))
    assert fn_count_dict['div'] == r3

    assert fn_count_dict == {'div': r3, 'mul': r2, 'add': r1}


def test_fn_run_counter_1_functionality():
    count_add = fn_run_counter_1(add)
    count_mul = fn_run_counter_1(mul)
    count_div = fn_run_counter_1(div)
    random_int = random.randint(1, 10)
    assert random_int + random_int == count_add(random_int, random_int)
    assert random_int * random_int == count_mul(random_int, random_int)
    assert random_int / random_int == count_div(random_int, random_int)


def test_fn_run_counter_1_inputs():
    with pytest.raises(TypeError):
        count_add = fn_run_counter_1('abc')
        count_add(1, 3)
    with pytest.raises(TypeError):
        count_add = fn_run_counter_1(add)
        count_add(1, 'r')
    with pytest.raises(ZeroDivisionError):
        count_div = fn_run_counter_1(div)
        count_div(1, 0)


def test_fn_run_counter_2_is_closure():
    fn = fn_run_counter_2(add, {})
    assert fn.__closure__


def test_fn_run_counter_2_add_count_pos():
    d = {}
    count_add = fn_run_counter_2(add, d)
    r = random.randint(1, 10)
    for i in range(r):
        count_add(random.random(), random.random())
    assert d['add'] == r


def test_fn_run_counter_2_mul_count_pos():
    d = {'mul': 2}
    count_mul = fn_run_counter_2(mul, d)
    r = random.randint(1, 10)
    for i in range(r):
        count_mul(random.random(), random.random())
    print(d)
    assert d['mul'] == r + 2


def test_fn_run_counter_2_div_count_pos():
    d = {'add': 3}
    count_div = fn_run_counter_2(div, d)
    r = random.randint(1, 10)
    for i in range(r):
        count_div(random.randint(1, 10), random.randint(1, 10))
    assert d['div'] == r and d['add'] == 3


def test_fn_run_counter_2_add_count_neg():
    d = {}
    count_add = fn_run_counter_2(add, d)
    r = random.randint(1, 10)

    for i in range(r):
        count_add(random.random(), random.random())
    assert not d.get('mul') and not d.get('div')


def test_fn_run_counter_2_count_all():
    d1 = {}
    count_add = fn_run_counter_2(add, d1)
    count_mul = fn_run_counter_2(mul, d1)
    count_div = fn_run_counter_2(div, d1)

    r1 = random.randint(1, 10)
    for i in range(r1):
        count_add(random.random(), random.random())
    assert d1['add'] == r1

    r2 = random.randint(1, 10)
    for i in range(r2):
        count_mul(random.random(), random.random())
    assert d1['mul'] == r2

    r3 = random.randint(1, 10)
    for i in range(r3):
        count_div(random.randint(1, 10), random.randint(1, 10))
    assert d1['div'] == r3

    assert d1 == {'div': r3, 'mul': r2, 'add': r1}

    d2 = {}
    count_add = fn_run_counter_2(add, d2)
    count_mul = fn_run_counter_2(mul, d2)
    count_div = fn_run_counter_2(div, d2)

    r1 = random.randint(11, 20)
    for i in range(r1):
        count_add(random.random(), random.random())
    assert d2['add'] == r1

    r2 = random.randint(11, 20)
    for i in range(r2):
        count_mul(random.random(), random.random())
    assert d2['mul'] == r2

    r3 = random.randint(11, 20)
    for i in range(r3):
        count_div(random.randint(1, 10), random.randint(1, 10))
    assert d2['div'] == r3

    assert d2 == {'div': r3, 'mul': r2, 'add': r1}
    assert d1 != d2


def test_fn_run_counter_2_inputs():
    with pytest.raises(TypeError):
        count_add = fn_run_counter_2('abc', {})
        count_add(1, 3)
    with pytest.raises(TypeError):
        count_add = fn_run_counter_2('abc', 'd')
        count_add(1, 3)
    with pytest.raises(TypeError):
        count_add = fn_run_counter_2(add, {})
        count_add(1, 'r')
    with pytest.raises(ZeroDivisionError):
        count_div = fn_run_counter_2(div, {})
        count_div(1, 0)
