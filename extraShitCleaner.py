def shitCleaner(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    unique_lines = []
    line_count = {}
    # شمارش تکرار هر خط
    for line in lines:
        line = line.strip()  # حذف فاصله‌های اضافی
        if line:  # اگر خط خالی نبود
            if line in line_count:
                line_count[line] += 1
            else:
                line_count[line] = 1
                unique_lines.append(line)  # تنها خطوط یکتا را نگه‌داری می‌کنیم

    # نوشتن خطوط یکتا به فایل جدید
    with open(file_path, 'w+') as output_file:
        for line in unique_lines:
            output_file.write(line + '\n')
    print(f"Duplicate lines removed. Unique lines saved in '{file_path}'.")