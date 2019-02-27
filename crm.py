from contact import Contact

class CRM:

  def main_menu(self):
   while True:
    self.print_main_menu()
    user_selected = int(input())
    self.call_option(user_selected)

  def print_main_menu(self):
   print('[1] Add a new contact')
  print('[2] Modify an existing contact')
  print('[3] Delete a contact')
  print('[4] Display all the contacts')
  print('[5] Search by attribute')
  print('[6] Exit')
  print('Enter a number: ')


  def call_option(self):
    if user_selected == 1:
     self.add_new_contact()
    elif user_selected == 2:
     self.modify_existing_contact()
    elif user_selected == 3:
     self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
       self.search_by_attribute()
elif user_selected ==6:
        quit()


  def add_new_contact(self):
   print('Enter First Name: ')
  first_name = input()

  print('Enter Last Name: ')
  last_name = input()

  print('Enter Email Address: ')
  email = input()

  print('Enter a Note: ')
  note = input()
 new_contact = Contact.create(first_name, last_name, email, note)

  def modify_existing_contact(self):
   user_id = int(intput("enter the id to update."))
   select_contact = Contact.find(user.id)

   print("Select an attribute you want to change")
   print("1 - First Name")
   print("2 - Last Name")
   print("2 - Email")
   print("4 - Note")
   attribute = int(input('enter the attribute that is going to change'))

  def delete_contact(self):
  print("To delete your contact information, please enter your contact information")
  delete_contact = int(input())
  current_contact = Contact.get(delete_contact)
  current_contact.delete_instance()
  print("contact information has been deleted")


  def display_all_contacts(self):
      for info in Contact.select():
          print(i.full_name())

  def search_by_attribute(self):
      print("which attribute would you like to see?")
      attribute_input = input()

      print("What value are you searching")
      value_input = input()

      print("This is the information: {}". format(Contact.find_by(attribute_input, value_input)))

      a_crm_app = CRM()
a_crm_app.main_menu()
