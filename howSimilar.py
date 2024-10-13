def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = set(f.read().splitlines())  # استفاده از مجموعه (set) برای حذف داده‌های تکراری
    return data

def calculate_similarity(file1, file2):
    # خواندن داده‌های هر فایل
    data1 = read_file(file1)
    data2 = read_file(file2)

    # محاسبه داده‌های مشترک
    common_data = data1.intersection(data2)

    # محاسبه درصد مشابهت
    total_data = len(data1.union(data2))
    similarity_percentage = (len(common_data) / total_data) * 100 if total_data > 0 else 0

    return len(common_data), similarity_percentage

# مسیر فایل‌ها را وارد کنید
file1 = 'export/mehr/19/MergedData.txt'
file2 = 'export/mehr/20/MergedData.txt'

common_count, similarity_percentage = calculate_similarity(file1, file2)

print(f'تعداد داده‌های مشترک: {common_count}')
print(f'درصد مشابهت: {similarity_percentage:.2f}%')