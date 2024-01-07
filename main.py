import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def example_function(x, y):
    return x + y

def run_tests():

    result, execution_time = measure_time(example_function, 3, 4)
    print(f"Результат: {result}, Час виконання: {execution_time} seconds")

    result, execution_time = measure_time(example_function, 5, 10)
    print(f"Результат: {result}, Час виконання: {execution_time} seconds")

if __name__ == "__main__":
    run_tests()