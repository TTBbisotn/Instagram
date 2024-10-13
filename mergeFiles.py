import os

def merge_files_in_directory(directory_path, output_file):
    all_data = set()  # مجموعه برای نگهداری داده‌ها بدون تکرار

    # خواندن تمامی فایل‌های موجود در پوشه
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # چک می‌کنیم که فایل باشد (نه پوشه)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_data = f.read().splitlines()
                all_data.update(file_data)  # افزودن داده‌های فایل به مجموعه (بدون تکرار)

    # ذخیره کردن اطلاعات مرج‌شده در یک فایل جدید
    output_path = os.path.join(directory_path, output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(all_data)))  # داده‌ها را مرتب کرده و در فایل خروجی می‌نویسیم

    print(f'تمامی اطلاعات فایل‌ها با هم ادغام شد و در فایل "{output_file}" ذخیره شد.')

# مسیر پوشه و نام فایل خروجی را وارد کنید
directory = 'export/mehr/21'
output_filename = 'MergedData.txt'

merge_files_in_directory(directory, output_filename)