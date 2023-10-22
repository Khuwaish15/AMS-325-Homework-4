import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def create_grid(rows, cols):
    return np.zeros((rows, cols), dtype=bool)

def initialize_glider(grid):
    # Place the Glider pattern near the middle of the grid
    middle_row, middle_col = grid.shape[0] // 2, grid.shape[1] // 2
    glider = np.array([[0, 1, 0],
                      [0, 0, 1],
                      [1, 1, 1]], dtype=bool)
    grid[middle_row:middle_row+3, middle_col:middle_col+3] = glider

def update_grid(grid):
    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            cell = grid[i, j]
            neighbors = [
                grid[(i - 1) % rows, (j - 1) % cols],
                grid[(i - 1) % rows, j],
                grid[(i - 1) % rows, (j + 1) % cols],
                grid[i, (j - 1) % cols],
                grid[i, (j + 1) % cols],
                grid[(i + 1) % rows, (j - 1) % cols],
                grid[(i + 1) % rows, j],
                grid[(i + 1) % rows, (j + 1) % cols]
            ]
            live_neighbors = sum(neighbors)

            if cell:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i, j] = False
            else:
                if live_neighbors == 3:
                    new_grid[i, j] = True

    return new_grid

def visualize_grid(grid, k, output_image, output_animation):
    fig, ax = plt.subplots()
    ims = []

    for step in range(k):
        if step % 10 == 0:
            im = ax.imshow(grid, cmap='binary', interpolation='nearest', animated=True)
            ims.append([im])
        
        grid = update_grid(grid)

    ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True, repeat=False)
    ani.save(output_animation, writer='pillow', fps=10)
    plt.savefig(output_image, format='png', dpi=300)
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python game_of_life.py <k>")
        sys.exit(1)

    try:
        k = int(sys.argv[1])
        if k <= 0:
            raise ValueError("k must be a positive integer")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    rows, cols = 50, 50  # You can adjust the size of the grid here

    initial_grid = create_grid(rows, cols)
    initialize_glider(initial_grid)

    output_image = 'game_of_life.png'
    output_animation = 'game_of_life.gif'

    visualize_grid(initial_grid, k, output_image, output_animation)
