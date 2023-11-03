def input_bug_counts(bug_type):
    count = int(input(f"Please enter the amount of {bug_type} bugs: "))
    return count

def calculate_percent(count, total):
    percent = (count/total)
    return percent

def input_bug_type_and_count():
    type = input("Please enter the type of bug: ")
    counts = input_bug_counts(type)
    return type, counts              

def display_table(bug1, count1, bug2, count2, bug3, count3): 
    total = count1 + count2 + count3
    print(f"{'Bug Type':<15} {'Count':>10} {'Percentage':>20}")
    print("="*50)
    print(f"{bug1:<15} {count1:>10} {calculate_percent(count1, total):>20.2%}")
    print(f"{bug2:<15} {count2:>10} {calculate_percent(count2, total):>20.2%}")
    print(f"{bug3:<15} {count3:>10} {calculate_percent(count3, total):>20.2%}")
    print("="*50)
    print(f"{'TOTAL':<15} {total:>10} {'100%':>20}")

bug1, count1 = input_bug_type_and_count()
bug2, count2 = input_bug_type_and_count()
bug3, count3 = input_bug_type_and_count()

display_table(bug1, count1, bug2, count2, bug3, count3)




