
import multiprocessing
import time
from multiprocessing import Pool, Lock, Manager

def process_customer(args):
    line_type, line_id, customer, output_lock = args
    with output_lock:
        print(f"{line_type} Line {line_id} processing customer {customer}...")
    time.sleep(0.1)  # Simulating processing time
    with output_lock:
        print(f"{line_type} Line {line_id} finished processing customer {customer}.")

def cashier(line_type, line_id, customers, output_lock):
    with output_lock:
        print(f"Line {line_id} of {line_type} starts processing.")
    
    for customer in customers:
        process_customer((line_type, line_id, customer, output_lock))
    
    with output_lock:
        print(f"Line {line_id} of {line_type} has finished processing.")

def main():
    manager = Manager()
    output_lock = manager.Lock()

    total_self_checkout_customers = int(input('\nEnter total self-checkout customers: '))
    total_traditional_checkout_customers = int(input('Enter total traditional customers: '))
    fifteen_item_checkout_customers = int(input('Enter total 15_item_checkout customers: '))

    print('\n')

    self_checkout_lines = 4
    traditional_lines = 2

    distributed_self_checkout_customers = [[] for _ in range(self_checkout_lines)]
    for i in range(total_self_checkout_customers):
        distributed_self_checkout_customers[i % self_checkout_lines].append(i + 1)

    distributed_traditional_customers = [[] for _ in range(traditional_lines)]
    for i in range(total_traditional_checkout_customers):
        distributed_traditional_customers[i % traditional_lines].append(i + 1)

    fifteen_item_customers = list(range(1, fifteen_item_checkout_customers + 1))

    tasks = []
    for i, customers in enumerate(distributed_self_checkout_customers):
        tasks.append(("Self-Checkout", i+1, customers, output_lock))
    for i, customers in enumerate(distributed_traditional_customers):
        tasks.append(("Traditional-Cashier", i+1, customers, output_lock))
    tasks.append(("15-or-less-item-cashier", 1, fifteen_item_customers, output_lock))

    start = time.perf_counter()

    with Pool() as pool:
        pool.starmap(cashier, tasks)

    finish = time.perf_counter()

    print(f'\nRuntime in: {round(finish-start, 2)} second(s)')

if __name__ == "__main__":
    main()
