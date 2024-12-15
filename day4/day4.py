class Day4Advent():
    def __init__(self, file_path):
        self.grid = open(file_path).read().splitlines()
        self.n = len(self.grid) # number of rows
        self.m = len(self.grid[0]) # number of columns
        self.part1 = 0
        self.part2 = 0
        
    def xmas_search(self):
        """Search for the word 'XMAS' in the word search."""
        self._horizontal_search()
        self._vertical_search()
        self._SW_diag_search()
        self._SW_diag_search()
        
    def _horizontal_search(self):
        """Search for the word 'XMAS' in the rows of the word search."""
        for row in self.grid:
            for j in range(self.m - 3):
                if row[j : j + 4] in ['XMAS','SAMX']:
                    self.part1 += 1

    def _vertical_search(self):
        """Search for the word 'XMAS' in the columns of the word search."""
        for col in zip(*self.grid):
            for i in range(self.n - 3):
                if ''.join(col[i : i + 4]) in ['XMAS', 'SAMX']:
                    self.part1 += 1

                        
    def _SW_diag_search(self):   
        """Search for the word 'XMAS' in down-left diagonals of the word search."""
        for i in range(self.n - 3):
            for j in range(3, self.m):
                word = self.grid[i][j] + self.grid[i + 1][j - 1] + self.grid[i + 2][j - 2] + self.grid[i + 3][j - 3]          
                if word in ['XMAS', 'SAMX']:
                    self.part1 += 1                    
                    
    def _SE_diag_search(self):   
        """Search for the word 'XMAS' in down-right diagonals of the word search."""
        for i in range(self.n - 3):
            for j in range(self.m - 3):
                word = self.grid[i][j] + self.grid[i + 1][j + 1] + self.grid[i + 2][j + 2] + self.grid[i + 3][j + 3]          
                if word in ['XMAS', 'SAMX']:
                    self.part1 += 1
                

         
         
if __name__ == '__main__':
    day4_example = Day4Advent('example.txt')
    day4_example.xmas_search()
    print(day4_example.part1, day4_example.part2)
    
    day4 = Day4Advent('input.txt')
    day4.xmas_search()
    print(day4.part1, day4.part2)
    
    