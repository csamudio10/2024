class Day2:
    def __init__(self, file_path: str):
        self.reports = []
        self.unsafe_reports = []
        self.file_path = file_path
        
        with open(file_path, 'r') as file:
            # Read the file line by line, converting each line into a list of integers
            self.reports = [list(map(int, line.split(" "))) for line in file] 
        
        self.part1_safe = 0
        self.part2_safe = 0
        
    def safety_check(self):
        for report in self.reports:
            increase_check = self.all_increasing(report)
            decrease_check = self.all_decreasing(report)
            
            if increase_check is True or decrease_check is True:
                self.part1_safe += 1
                self.part2_safe += 1
            else:
                self.unsafe_reports.append(report)
                    
    def all_increasing(self, report: list):
        safe = True
        for j in range(len(report) - 1):
            if report[j+1] - report[j] > 3 or report[j+1] - report[j] < 1:
                safe = False
                break
        return safe


    def all_decreasing(self, report: list):
        safe = True
        for j in range(len(report) - 1):
            if report[j] - report[j+1] > 3 or report[j] - report[j+1] < 1:
                safe = False
                break
        return safe
    
    def damp_level(self):
        for report in self.unsafe_reports:
            for i in range(len(report)):
                increase_check = self.all_increasing(report[:i] + report[i+1:])
                decrease_check = self.all_decreasing(report[:i] + report[i+1:])
                if increase_check is True or decrease_check is True:
                    self.part2_safe += 1
                    break




if __name__ == '__main__':
    day2 = Day2('day2_input.txt')
    day2.safety_check()
    day2.damp_level()
    print(day2.part1_safe, day2.part2_safe)   
    