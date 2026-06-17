import multiprocessing
import time


def is_prime(n: int) -> bool:
    """Função para verificação de primalidade."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def find_max_prime_sequential(timeout: int) -> int:
    """Procura o maior número primo sequencialmente até ao limite temporal."""
    start_time = time.time()
    max_prime = 2
    current_num = 3

    while time.time() - start_time < timeout:
        if is_prime(current_num):
            max_prime = current_num
        current_num += 2  # Apenas números ímpares para eficiência

    return max_prime


def worker_find_prime(start_num, step, timeout, start_time, shared_max, lock):
    """Função executada por cada worker em paralelo."""
    current_num = start_num
    while time.time() - start_time < timeout:
        if is_prime(current_num):
            with lock:
                if current_num > shared_max.value:
                    shared_max.value = current_num
        current_num += step


def find_max_prime_parallel(timeout: int, workers: int) -> int:
    """Procura o maior número primo usando múltiplos processos workers."""
    shared_max = multiprocessing.Value('i', 2)
    lock = multiprocessing.Lock()
    start_time = time.time()

    processes = []

    # Divisão do espaço de procura por saltos
    for i in range(workers):
        start_num = 3 + (i * 2)
        step = workers * 2
        p = multiprocessing.Process(
            target=worker_find_prime,
            args=(start_num, step, timeout, start_time, shared_max, lock)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return shared_max.value


if __name__ == "__main__":
    T = 2
    print(f"Procura iniciada ({T}s)...")
    print("Sequencial:", find_max_prime_sequential(T))
    print("Paralelo:", find_max_prime_parallel(T, 4))