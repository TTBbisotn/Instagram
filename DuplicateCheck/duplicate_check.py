def find_duplicate_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_count = {}
    # شمارش تکرار هر خط
    for line in lines:
        line = line.strip()  # حذف فاصله‌های اضافی
        if line:  # اگر خط خالی نبود
            if line in line_count:
                line_count[line] += 1
            else:
                line_count[line] = 1
    # چاپ نتایج
    for line, count in line_count.items():
        if count >= 1:
            print(f"'{line}' occurs {count} times")

# مسیر فایل را به تابع بدهید
# file_path = 'Storydata(noDuplicate).txt'  # مسیر فایل متنی خود را وارد کنید
# file_path = 'Storydata.txt'  # مسیر فایل متنی خود را وارد کنید

# find_duplicate_lines('pureData/pure1Storydata.txt')