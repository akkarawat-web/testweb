attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],  # Day 1
    ["Alice", "Charlie", "David"],         # Day 2
    ["Alice", "Bob", "David"],             # Day 3
    ["Alice", "David", "Eve"],             # Day 4
    ["Bob", "Charlie", "David"]            # Day 5
]

attendance_sets = [set(day) for day in attendance_week]

all_days_present = set.intersection(*attendance_sets)
print(" Present every day:", all_days_present)

all_students = set.union(*attendance_sets)
absent_at_least_one_day = all_students - all_days_present
print(" Absent at least one day:", absent_at_least_one_day)

day1_not_day5 = list(attendance_sets[0] - attendance_sets[-1])
print(" Present day 1 but absent last day:", day1_not_day5)

unique_students = len(all_students)
print("Total unique students:", unique_students)