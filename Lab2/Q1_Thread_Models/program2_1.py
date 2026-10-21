import threading
import time

TASKS = [
    ("Task 1",1),
    ("Task 2",1),
    ("Task 3",1),
]
   
def do_task(task_name,wait_time):
    thread_id = threading.get_ident()
    
    print(f"{task_name}STARTED | thread ID = {thread_id}")
    time.sleep(wait_time)
    print(f"{task_name}FINISHED | thread ID = {thread_id}")
    
def single_threaded():
    print("\n========SINGLE-THREADED========")
    
    start_time = time.perf_counter()
    
    for task_name,wait_time in TASKS:
        do_task(task_name,wait_time)
        
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        
        print(f"Single-Threaded time = {elapsed:.2f} seconds")
        return elapsed
    
def multithreaded():
    print("\n========MULTITHREADED========")
    
    start_time = time.perf_counter()
    threads = []
    
    for task_name,wait_time in TASKS:
        thread = threading.Thread(
            target= do_task,
            args=(task_name,wait_time)
        )
        
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    
    print(f"Multithreaded time = {elapsed:.2f} seconds")
    return elapsed

def main():
    single_time = single_threaded()
    multi_time = multithreaded()
    
    print("\n========COMPARSION========")
    print(f"Single-threaded : {single_time:.2f} seconds")
    print(f"Multi-threaded : {multi_time:.2f} seconds")
    
    print("\nAll worker threads completed successfully.")
    
if __name__ == "__main__":
    main()
