import re

class Day3():
    def __init__(self, file_path):
        self.part1_total = 0
        with open(file_path, "r", encoding="utf-8") as file:
            # Read the file contents into a string
            self.txt = file.read()
    
        self.part1_total = self.part1(self.txt)
        self.part2_total = self.damp(self.txt)
        
    
    
    def part1(self, puzzle_input):
        self.part1_total = 0
        for a, b in re.findall(r"mul\((\d+),(\d+)\)", puzzle_input):
            self.part1_total += int(a) * int(b)
            
        return self.part1_total
            
            
    def damp(self, puzzle_input):
        do = r"do\(\)"
        dont = r"don't\(\)"
        mul = r"mul\((\d+),(\d+)\)"
        total = 0
        enabled = True
        for x in re.finditer(f'{do}|{dont}|{mul}', puzzle_input):
            if re.fullmatch(do, x.group()):
                enabled = True
            elif re.fullmatch(dont, x.group()):
                enabled = False
            elif enabled:
                total += int(x.group(1)) * int(x.group(2))

        return total

d3p1 = Day3('day3_input.txt')

print(d3p1.part1_total)

print(d3p1.part2_total)


d3_example = Day3('day3_example.txt')
