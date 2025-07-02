# import re
#
# class Contact:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
# class ContactManager:
#     def __init__(self):
#         self.contacts = []
#
#     def is_valid_phone(self, phone):
#         pattern = r'^(\+998|998)[0-9]{9}$'
#         return re.match(pattern, phone)
#
#     def add_contact(self, name, phone):
#         if self.is_valid_phone(phone):
#             self.contacts.append(Contact(name, phone))
#             print(f" {name} ({phone}) kontaktga qo‘shildi.")
#         else:
#             print(" Noto‘g‘ri raqam formati!")
#
#     def get_contact_by_phone(self, phone):
#         for contact in self.contacts:
#             if contact.phone == phone:
#                 return contact
#         return None
#
#     def show_contacts(self):
#         print("\nKontaktlar ro‘yxati:")
#         if not self.contacts:
#             print(" - Kontakt qo‘shilmagan.")
#         else:
#             for contact in self.contacts:
#                 print(f" + {contact.name}: {contact.phone}")
#
#
# class SMSManager:
#     def __init__(self, contact_manager):
#         self.contact_manager = contact_manager
#         self.sms_history = []
#
#     def send_sms(self, phone, message):
#         if not self.contact_manager.is_valid_phone(phone):
#             print(" Noto‘g‘ri raqam formati!")
#             return
#         contact = self.contact_manager.get_contact_by_phone(phone)
#         if contact:
#             self.sms_history.append({'to': phone, 'message': message})
#             print(f" SMS {contact.name} ({phone}) ga yuborildi.")
#         else:
#             print(" Bu raqam kontaktlar ro‘yxatida yo‘q!")
#
# class App:
#     def __init__(self):
#         self.contact_manager = ContactManager()
#         self.sms_manager = SMSManager(self.contact_manager)
#
#     def run(self):
#         while True:
#             print("\n Dasturga xush kelibsiz!")
#             print("1. Kontakt Menejer")
#             print("2. SMS Menejer")
#             print("3. Kontaktlar ro‘yxatini ko‘rish")
#             print("4. Chiqish")
#             choice = input("Tanlang (1/2/3/4): ")
#
#             if choice == '1':
#                 self.run_contact_manager()
#             elif choice == '2':
#                 self.run_sms_manager()
#             elif choice == '3':
#                 self.contact_manager.show_contacts()
#             elif choice == '4':
#                 print(" Chiqildi.")
#                 break
#             else:
#                 print(" Noto‘g‘ri tanlov!")
#
#     def run_contact_manager(self):
#         while True:
#             print("\n--- Kontakt Menejer ---")
#             name = input("Ism kiriting (yoki 'chiqish'): ")
#             if name.lower() == 'chiqish':
#                 break
#             phone = input("Telefon raqami kiriting (+998...): ")
#             self.contact_manager.add_contact(name, phone)
#
#
#
#     def run_sms_manager(self):
#         if not self.contact_manager.contacts:
#             print(" Avval kontakt qo‘shing.")
#             return
#         while True:
#             print("\n--- SMS Menejer ---")
#             phone = input("Telefon raqami (yoki 'chiqish'): ")
#             if phone.lower() == 'chiqish':
#                 break
#             message = input("SMS matnini yozing: ")
#             self.sms_manager.send_sms(phone, message)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.run()
