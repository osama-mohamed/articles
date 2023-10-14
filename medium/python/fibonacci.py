def fibonacci(num):
  if num == 0:
    return 0
  if num == 1:
    return 1
  return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(7))


def fib(n):
  return 1 if n == 1 else 0 if n == 0 else fib(n - 1) + fib(n - 2)
print(fib(7))


def fibonacci_cached(step, _cache={}):
  if step in _cache:
    return _cache[step]
  elif step > 1:
    return _cache.setdefault(step, fibonacci_cached(step - 1) + fibonacci_cached(step - 2))
  return step
print(fibonacci_cached(7))


def fibonacci_cached_two(step, _cache={}):
  if step in _cache:
    return _cache[step]
  if step == 0:
    return 0
  if step == 1:
    return 1
  _cache[step] = fibonacci_cached_two(step - 1, _cache) + fibonacci_cached_two(step - 2, _cache)
  return _cache[step]
print(fibonacci_cached_two(7))


def fibonacci_for_list(n):
  fib_list = [0, 1]
  for num in range(2, n + 1):
    fib_list.append(fib_list[num - 1] + fib_list[num - 2])
  return fib_list[n]
print(fibonacci_for_list(7))


def fibonacci_for_variable(n):
  num1, num2 = 0, 1
  for _ in range(n):
    num1, num2 = num2, num1 + num2
  return num1
print(fibonacci_for_variable(7))


def fibonacci_while(n):
  num1, num2 = 0, 1
  counter = 0
  fib_list = [num1]
  while counter < n:
    num1, num2 = num2, num1 + num2
    fib_list.append(num1)
    counter += 1
  return num1
print(fibonacci_while(7))