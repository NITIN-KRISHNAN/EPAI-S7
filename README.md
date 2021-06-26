# EPAI Session 7 - Scopes and Closures

## Assignment problem statement
1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50
   characters. 50 is stored as a free variable (+ 4 tests) - 200
2. Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how
   many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250

## Description of Functions in Assignment
### doc_string_validator
Closure to validate that given input function has a doc string of min length 50 characters
param fn: input function

return
- False
  - char length of doc string is less than or equal to 50
  - no doc string
- True when its length of doc string is greater than 50 

raises: TypeError when input is not a function
### gen_next_fib_num
closure to generate the next Fibonacci number

return the next Fibonacci number
### fn_run_counter
closure to count the number of times a function is executed

param fn: input function

return: closure
### add
function to add two numbers

param a: first input number

param b: second input number

return: sum of the input numbers
### mul
function to multiply two numbers

param a: first input number 

param b: second input number 

return: product of the input numbers
### div
function to divide two numbers

param a: first input number

param b: second input number

return: result of division of the first input number by second input number
### fn_run_counter_1
Closure to count the number of times a function is called and store the result in a global dict 

param fn:input function	

return:closure

raises: TypeError when input is not a function
### fn_run_counter_2
Closure to count the number of times a function is called and store the result in the dict provided as input 

param fn:input function 

param dict_n:dictionary to store the corresponding functions execution count 

return:closure

raise: TypeError whe fn is not a function or dict_n is not a dictionary
## Description of Test cases
|#   | Test name  | Test description   |
|---|---|---|
| 1  | test_function_names  | checks if any of the functions contains an upper cases letter  |
|  2 | test_readme_exists  | checks if read me file exists  |
|  3 | test_readme_proper_description  | checks if README.md describes all the functions  |
|  4 |  test_readme_file_for_formatting | checks if README.md is properly formatted   |
|  5 |  test_indentations | checks if the code file has proper indentation  |
|  6 | test_doc_string_validator_positive  |  checks if doc_string_validator closure gives correct value of True when a function with > 50 char doc string is passed |
|  7 | test_doc_string_validator_negative  |  checks if doc_string_validator closure gives correct value of False when a function with < 50 char doc string is passed |
| 8 | test_doc_string_validator_none  | checks if doc_string_validator closure gives correct value of False when a function with no char doc string is passed   |
|  9 | test_doc_string_validator_non_function  | checks if the doc_string_validator closure raises TypeError when a non function is passed as parameter |
|  10 |  test_doc_string_validator_is_closure |  checks if is an closure |
|  11 | test_gen_next_fib  |  checks if the first 5 generated Fibonacci numbers are correct |
|  12 | test_gen_next_fib_1  |  checks if the result is same when two different instances of the closure are used to generate the next Fibonacci number |
|  13 |   test_gen_next_fib_is_closure| checks if gen_next_fib is a closure  |
|  14 |test_fn_run_counter_1_is_closure   | checks if fn_run_counter_1 is a closure   |
|  15 | test_fn_run_counter_1_add_count_pos  | checks if the add function run count is correct when run for a random number of times   |
|  16 | test_fn_run_counter_1_mul_count_pos   | checks if the mul function run count is correct when run for a random number of times   |
|  17 | test_fn_run_counter_1_div_count_pos  |   checks if the div function run count is correct when run for a random number of times   |
|  18 | test_fn_run_counter_1_add_count_neg  |  checks if no function that is not run is added to the global function count dictionary |
|  19 |  test_fn_run_counter_1_count_all | checks if the function run count is correct for combination for all 3 add, div, mul functions  |
|  20 | test_fn_run_counter_1_functionality  | checks the functionality of add, mul abd div functions  |
|  21 | test_fn_run_counter_1_inputs  |  checks if the input given to fn_run_counter_1 closure if correct, i.e. a function is sent as argument |
|  22 |  test_fn_run_counter_2_is_closure |  checks if fn_run_counter_2 is a closure   |
|  23 |  test_fn_run_counter_2_add_count_pos |  checks if the add function run count is correct when run for a random number of times in the dict that is sent as parameter  |
|  24 |  test_fn_run_counter_2_mul_count_pos |  checks if the mul function run count is correct when run for a random number of times in the dict that is sent as parameter |
|  25 |  test_fn_run_counter_2_div_count_pos |  checks if the div function run count is correct when run for a random number of times in the dict that is sent as parameter |
|  26 | test_fn_run_counter_2_add_count_neg  |checks if no function that is not run is added in the dict that is sent as parameter   |
|  27 | test_fn_run_counter_2_count_all  |checks if the function run count is correct for combination for all 3 add, div, mul functions in the dict that is sent as parameter   |
|  28 |  test_fn_run_counter_2_inputs |  checks if the input given to fn_run_counter_1 closure if correct, i.e. a function is sent as first argument and dict is sent as second argument |

## Test Results
### Output of  pytest -r test_closures.py 
================================================================= test session starts ==================================================================

platform darwin -- Python 3.8.1, pytest-6.2.4, py-1.10.0, pluggy-0.13.1

plugins: Faker-4.1.3

collected 28 items               

test_closures.py ............................[100%]

=============================================================== short test summary info ================================================================

PASSED test_closures.py::test_function_names

PASSED test_closures.py::test_readme_exists

PASSED test_closures.py::test_readme_proper_description

PASSED test_closures.py::test_readme_file_for_formatting

PASSED test_closures.py::test_indentations

PASSED test_closures.py::test_doc_string_validator_positive

PASSED test_closures.py::test_doc_string_validator_negative

PASSED test_closures.py::test_doc_string_validator_none

PASSED test_closures.py::test_doc_string_validator_non_function

PASSED test_closures.py::test_doc_string_validator_is_closure

PASSED test_closures.py::test_gen_next_fib

PASSED test_closures.py::test_gen_next_fib_1

PASSED test_closures.py::test_gen_next_fib_is_closure

PASSED test_closures.py::test_fn_run_counter_1_is_closure

PASSED test_closures.py::test_fn_run_counter_1_add_count_pos

PASSED test_closures.py::test_fn_run_counter_1_mul_count_pos

PASSED test_closures.py::test_fn_run_counter_1_div_count_pos

PASSED test_closures.py::test_fn_run_counter_1_add_count_neg

PASSED test_closures.py::test_fn_run_counter_1_count_all

PASSED test_closures.py::test_fn_run_counter_1_functionality

PASSED test_closures.py::test_fn_run_counter_1_inputs

PASSED test_closures.py::test_fn_run_counter_2_is_closure

PASSED test_closures.py::test_fn_run_counter_2_add_count_pos

PASSED test_closures.py::test_fn_run_counter_2_mul_count_pos

PASSED test_closures.py::test_fn_run_counter_2_div_count_pos

PASSED test_closures.py::test_fn_run_counter_2_add_count_neg

PASSED test_closures.py::test_fn_run_counter_2_count_all

PASSED test_closures.py::test_fn_run_counter_2_inputs

================================================================== 28 passed in 0.16s ==================================================================

