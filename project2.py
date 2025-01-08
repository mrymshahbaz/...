import pandas as pd

data = {
    'کد ملی': [1557773895, 1234543210, 1540702121],
    'نام': ['ali', 'mohmd', 'amir'],
    'نام خانوادگی': ['akbari', 'shahbazi', 'ebrahimi'],
    'شماره تلفن': ['09126792479', '09308394934', '09216451827'],
    'ایمیل': ['ali.akbari@example.com', 'mohmd.shahbazi@example.com', 'amir.ebrahimi@example.com']
}

df = pd.DataFrame(data)
excel_file_path = '[/mnt/data/users.xlsx'](https://gapgpt.app/media/code_interpreter/0ea561c2-7244-44cf-bc0b-956cd214290c/users.xlsx')
df.to_excel(excel_file_path, index=False)

print(f"فایل اکسل با نام '{excel_file_path}' با موفقیت ایجاد شد.")


def find_user_by_national_code(national_code):
    try:
        df = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        return "فایل اکسل یافت نشد."

    user = df[df['کد ملی'] == national_code]

    if not user.empty:
        return user.to_dict(orient='records')[0]
    else:
        return "کاربری با این کد ملی یافت نشد."

national_code_to_find = 012345678
user_info = find_user_by_national_code(national_code_to_find)
print(user_info)

national_code_to_find = 0000111111
user_info = find_user_by_national_code(national_code_to_find)
print(user_info)

national_code_to_find = 5678901234
user_info = find_user_by_national_code(national_code_to_find)
print(user_info)