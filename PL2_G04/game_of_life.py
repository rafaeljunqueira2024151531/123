import multiprocessing
import copy

def count_neighbors(grid, r, c, rows, cols):
    """Conta os vizinhos vivos de uma célula (8 adjacentes)."""
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nr, nc = r + i, c + j
            if 0 <= nr < rows and 0 <= nc < cols:
                count += grid[nr][nc]
    return count

def update_slice(grid, start_row, end_row):
    """Calcula o próximo estado para um intervalo de linhas."""
    rows = len(grid)
    cols = len(grid[0])
    new_slice = []

    for r in range(start_row, end_row):
        new_row = []
        for c in range(cols):
            alive_neighbors = count_neighbors(grid, r, c, rows, cols)
            if grid[r][c] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_row.append(0)
                else:
                    new_row.append(1)
            else:
                if alive_neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_slice.append(new_row)
    return new_slice

def game_of_life_sequential(grid, generations):
    """Simulação sequencial do Game of Life."""
    current_grid = copy.deepcopy(grid)
    rows = len(current_grid)

    for _ in range(generations):
        current_grid = update_slice(current_grid, 0, rows)

    return current_grid

def game_of_life_parallel(grid, generations, workers):
    """Simulação paralela usando divisão por regiões."""
    current_grid = grid
    rows = len(grid)

    chunk_size = rows // workers
    intervals = []
    for i in range(workers):
        start = i * chunk_size
        end = rows if i == workers - 1 else (i + 1) * chunk_size
        intervals.append((start, end))

    with multiprocessing.Pool(processes=workers) as pool:
        for _ in range(generations):
            tasks = [(current_grid, start, end) for start, end in intervals]
            results = pool.starmap(update_slice, tasks)

            new_grid = []
            for slice_res in results:
                new_grid.extend(slice_res)
            current_grid = new_grid

    return current_grid

if __name__ == "__main__":
    initial_grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    gen = 5
    print(f"Simulação de {gen} gerações...")
    res_seq = game_of_life_sequential(initial_grid, gen)
    res_par = game_of_life_parallel(initial_grid, gen, 2)
    print("Consistência:", res_seq == res_par)