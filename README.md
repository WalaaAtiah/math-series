# LAB - Class 02

## Project: Modules and Testing

### Author: Walaa' Atiyh

## purpose of this code :
to write three function each function return nth number from math series 
  1.  Fibonacci Series:numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us: 0, 1, 1, 2, 3, 5, 8, 13, ...
    inpute : n "int"
    output : Fibonacci(n) "int"

  2. lucas_series:numeric series starting with the integers 2 and 1. In this series, the next integer is determined by summing the previous two. This gives us: 2, 1, 3, 4, 7, 11, 18, 29, ...
    inpute : n "int"
    output : lucas(n) "int"
  3. other series :
     inputs: n as required parameter and x,y as optional parameters which is the base case for the series "the first two number in the series "and have intial value x=0,y=1
     output :sum_series(n,x,y)

### Links and Resources

- [sololearn](https://www.sololearn.com/learning/1073)
  
### Setup

#### .venv requirements (for virtual environment)


#### How to initialize/run your application (where applicable)

* python series/series.py
* python -m series.series

#### How to use your library (where applicable)
   1- instal the library pytest
    pip insert pytest 
#### Tests

- How do you run tests?
   * "pytest" comand 
   * pytest test/test_series.py
  
- Any tests of note?no
- Describe any tests that you did not complete, skipped, etc  
  no ,all the test copmlete 

- how to run the test 
  1. pytest
  2. pytest tests/fib_iteration.py    
  3.  pytest tests/fib_recursion .py
  4. pytest tests/lucas-recursion.py
  5. pytest tests/sum_series.py



