import tkinter as tk
import random

class Tile:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color  # Color :타일 표시

class GridGUI:
    def __init__(self, root, grid_width, grid_height, cell_size):
        self.root = root
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.canvas = tk.Canvas(root, width=grid_width * cell_size, height=grid_height * cell_size)
        self.canvas.pack()

        # Initialize an empty grid
        self.grid = [['.' for _ in range(grid_width)] for _ in range(grid_height)]

    def can_place_tile(self, row, col, tile):
        """Check if the tile can be placed at the (row, col) position."""
        if row + tile.height > self.grid_height or col + tile.width > self.grid_width:
            return False  # 타일 주어진 공간 초과
        # 타일 찾는지 확인
        for i in range(tile.height):
            for j in range(tile.width):
                if self.grid[row + i][col + j] != '.':
                    return False
        return True

    def place_tile(self, row, col, tile):
        """Place a tile on the grid if it fits."""
        if self.can_place_tile(row, col, tile):
            for i in range(tile.height):
                for j in range(tile.width):
                    self.grid[row + i][col + j] = tile.color  # 포지션 컬러로 표시
                    # 타일 완성
                    x1 = (col + j) * self.cell_size
                    y1 = (row + i) * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=tile.color, outline="black")
            return True
        return False

    def simulate_random_tiling(self, num_tiles):
        """Simulate random tile placement."""
        colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']
        for _ in range(num_tiles):
            # 랜덤 타일 생성
            tile_width = random.randint(1, 3)
            tile_height = random.randint(1, 3)
            tile_color = random.choice(colors)
            tile = Tile(tile_width, tile_height, tile_color)

            # 채워질 때까지 랜덤
            placed = False
            while not placed:
                random_row = random.randint(0, self.grid_height - 1)
                random_col = random.randint(0, self.grid_width - 1)
                placed = self.place_tile(random_row, random_col, tile)


def main():
    root = tk.Tk()
    root.title("Tile Placement Simulation")

    # Grid settings
    grid_width = 10  # 열
    grid_height = 10  # 행
    cell_size = 50  

    grid_gui = GridGUI(root, grid_width, grid_height, cell_size)
    grid_gui.simulate_random_tiling(10) 

    root.mainloop()

if __name__ == "__main__":
    main()
