import time
from _multiprocessing import Proccess

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')

def complex_calculation():
    start = time.time()
    print('Starting calculating...')
    [x**2 for x in range(2000000)]
    print(f'complex_calculation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time:{time.time() - start}')

process = Proccess(target=complex_calculation)
process2 = Proccess(target=complex_calculation)
process.start()
process2.start()

start = time.time()

process.join()
process2.join()

print(f'Two process total time:{time.time() - start}')