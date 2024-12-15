# Function to read a text file
def import_text_file_as_list(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the file line by line, converting each line into a list of integers
            list_of_lists = [list(map(int, line.split(" "))) for line in file]
            return list_of_lists
    except FileNotFoundError:
        print(f"The file at '{file_path}' was not found.")
    except ValueError:
        print("The file contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    

def safety_check(reports: list, damp: bool = False):
    safe_count = 0
    if damp is False:
        for report in reports:
            increase_check = all_increasing(report)
            decrease_check = all_decreasing(report)
            
            if increase_check is True or decrease_check is True:
                safe_count += 1
                
                
    if damp is True:
        for report in reports:
            increase_check = damp_increasing(report)
            decrease_check = damp_decreasing(report)
            
            if increase_check is True or decrease_check is True:
                safe_count += 1
        
    
    return safe_count
        
        
            
def all_increasing(report: list):
    safe = True
    for j in range(len(report) - 1):
        if report[j+1] - report[j] > 3 or report[j+1] - report[j] < 1:
            safe = False
            break
    return safe


def all_decreasing(report: list):
    safe = True
    for j in range(len(report) - 1):
        if report[j] - report[j+1] > 3 or report[j] - report[j+1] < 1:
            safe = False
            break
    return safe



def damp_increasing(report: list, damp_count: int = 0):
    safe = True
    for j in range(len(report) - 1):
        if (report[j+1] - report[j] > 3 or report[j+1] - report[j] < 1):
            if damp_count > 0:
                safe = False
                return safe
            
            damped_list = report.copy()
            damped_list.pop(j+1)
            damped_check = damp_increasing(damped_list,damp_count = 1)
            if damped_check is False:
                safe = False
                break
    return safe


def damp_decreasing(report: list, damp_count: int = 0):
    safe = True
    for j in range(len(report) - 1):
        if report[j] - report[j+1] > 3 or report[j] - report[j+1] < 1:
            if damp_count > 0:
                safe = False
                return safe
            
            damped_list = report.copy()
            damped_list.pop(j+1)
            damped_check = damp_decreasing(damped_list,damp_count = 1)
            if damped_check is False:
                safe = False
                break
    return safe


# Specify the path to your text file
file_path = "day2_input.txt"

# Call the function and print the result
result = import_text_file_as_list(file_path)

#===================================== testing area ===================================================
a = [71, 73, 74, 76, 78, 80, 77]
print(damp_increasing(a))

# execution of the safety check
safe_count = safety_check(result,damp=True)

print(safe_count)

