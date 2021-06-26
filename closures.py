"""
Closures examples
"""
import types


def doc_string_validator(fn):
	"""
	closure to validate that given input function has a doc string of min length 50 characters
	:param fn: input function
	:return:
	False when  - char length of doc string is less than or equal to 50
				- no doc string
	True when it length of doc string is greater than 50
	:raises: TypeError when input is not a function
	"""
	char_count = 50

	def inner_function(*args, **kwargs):
		if not isinstance(fn, types.FunctionType):
			raise TypeError()
		if fn.__doc__ and len(fn.__doc__) > char_count:
			fn(*args, **kwargs)
			return True
		else:
			return False

	return inner_function


def gen_next_fib_num():
	"""
	closure to generate the next Fibonacci number
	:return: the next Fibonacci number
	"""
	penultimate_number = 0
	ultimate_number = 1

	def inner_function():
		nonlocal penultimate_number, ultimate_number
		tmp = ultimate_number
		ultimate_number = ultimate_number + penultimate_number
		penultimate_number = tmp
		return ultimate_number

	return inner_function


def fn_run_counter(fn):
	"""
	closure to count the number of times a function is executed
	:param fn: input function
	:return: closure
	"""
	count = 0

	def inner_function(*args, **kwargs):
		nonlocal count
		count = count + 1
		print(fn.__name__, " called ", count, " times ")
		return fn(*args, **kwargs)

	return inner_function


def add(a, b):
	"""
	function to add two numbers
	:param a: first input number
	:param b: second input number
	:return: sum of the input numbers
	"""
	return a + b


def mul(a, b):
	"""
	function to multiply two numbers
	:param a: first input number
	:param b: second input number
	:return: product of the input numbers
	"""
	return a * b


def div(a, b):
	"""
	function to divide two numbers
	:param a: first input number
	:param b: second input number
	:return: result of division of the first input number by second input number
	"""
	return a / b


# global dict to store the function's execution count
fn_count_dict = {}


def fn_run_counter_1(fn):
	"""
	Closure to count the number of times a function is called and store the result in a global dict
	:param fn:input function
	:return:closure
	:raises: TypeError when input is not a function
	"""
	if not (callable(fn) or isinstance(fn, types.FunctionType)):
		raise TypeError

	count = 0

	def inner_function(*args, **kwargs):
		nonlocal count
		count += 1
		print(fn.__name__, " called ", count, " times ")
		fn_count_dict[fn.__name__] = fn_count_dict.get(fn.__name__, 0) + 1
		return fn(*args, **kwargs)

	return inner_function


def fn_run_counter_2(fn, dict_n):
	"""
	Closure to count the number of times a function is called and store the result in the dict provided as input
	:param fn:input function
	:param dict_n:dictionary to store the corresponding functions execution count
	:return:closure
	:raise: TypeError whe fn is not a function or dict_n is not a dictionary
	"""
	if not (callable(fn) or isinstance(fn, types.FunctionType)) or not isinstance(dict_n, dict):
		raise TypeError
	count = 0

	def inner_function(*args, **kwargs):
		nonlocal count
		count += 1
		print(fn.__name__, " called ", count, " times ")
		dict_n[str(fn.__name__)] = dict_n.get(fn.__name__, 0) + 1
		return fn(*args, **kwargs)

	return inner_function
