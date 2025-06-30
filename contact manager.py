# import re
#
# contacts = {}
#
#
# def first_name(name):
#     code = r"^[A-Za-z]{2,20}$"
#     return re.match(code, name)
#
# def phone_number(phone):
#     code = r"^\+998\d{9}$"
#     return re.match(code, phone)
#
#
# def add_contact():
#     name = input("Ismni kiriting (faqat lotin harflari): ").strip()
#     if not first_name(name):
#         print("Ism noto‘g‘ri formatda. Qaytadan urinib ko‘ring.\n")
#         return
#
#     phone = input("Telefon raqamini kiriting (+998XXXXXXXXX): ").strip()
#     if not phone_number(phone):
#         print("Telefon raqami noto‘g‘ri formatda. Qaytadan urinib ko‘ring.\n")
#         return
#
#     contacts[name] = phone
#     print(f"{name} kontakti qo‘shildi.\n")
#
#
# def view_contact():
#     name = input("Ismni kiriting: ").strip()
#     if name in contacts:
#         print(f"{name} raqami: {contacts[name]}\n")
#     else:
#         print("Bunday kontakt mavjud emas.\n")
#
#
# def delete_contact():
#     name = input("O‘chirmoqchi bo‘lgan ismingizni kiriting: ").strip()
#     if name in contacts:
#         del contacts[name]
#         print(f"{name} kontakti o‘chirildi.\n")
#     else:
#         print("Bunday ism topilmadi.\n")
#
#
# def main():
#     while True:
#         print("=== Kontakt Menejeri ===")
#         print("1. Kontakt qo‘shish")
#         print("2. Kontaktni ko‘rish")
#         print("3. Kontaktni o‘chirish")
#         print("0. Chiqish\n")
#
#         kod = input("Tanlang: ").strip()
#
#         if kod == '1':
#             add_contact()
#         elif kod == '2':
#             view_contact()
#         elif kod == '3':
#
#
#             delete_contact()
#         elif kod == '0':
#             print("Dasturni yakunladingiz.")
#             break
#         else:
#             print("Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.\n")
#
#
# if __name__ == "__main__":
#     main()






import time


def log_info(func):
    def wrapper(*args, **kwargs):
        print(f"\n Funksiya: {func.__name__}")
        print(" Argumentlar:")
        for arg in args:
            print(f"  - Qiymat: {arg} | Turi: {type(arg)}")
        for key, value in kwargs.items():
            print(f"  - {key} = {value} | Turi: {type(value)}")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        duration = end - start
        print(f" Vaqt: {duration:.6f} soniya")
        return result

    return wrapper

@log_info
def add_contact(name, phone):
    print(f" {name} kontakti qo‘shildi.")

if __name__ == "__main__":
    add_contact("Ali", "+998901234567")
