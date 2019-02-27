class Contact:
  contacts = []
  next_id = 1

  def __init__(self, first_name, last_name, email, note):
    """This method should initialize the contact's attributes"""
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = Contact.next_id
    Contact.next_id += 1



  @classmethod
  def create(cls, first_name, last_name, email, note):
    """This method should call the initializer,
    store the newly created contact, and then return it
    """
    new_contact = Contact(first_name, last_name, email, note)
    cls.contacts.append(new_contact)
    return new_contact

  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
all_contacts = []
for item in cls.contacts:
 all_contacts.append(item)
return all_contacts

  @classmethod
  def find(cls, id):
    """ This method should accept an id as an argument
    and return the contact who has that id
    """
  find_contact = 0
  for contact in cls.contacts:
      if contact.id = id:
          find_contact = contact
      return find_contact
  else:
      return "couldn't fin contact"

  def update(self, attribute_change, new_value):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """
    if attribute_change not in ['first_name', 'last_name', 'email', 'note']:
        return False
    elif attribute_change == 'first_name':
        self.first_name = new_value
    elif attribute_change == 'last_name':
        self.last_name = new_value
    elif attribute_change == 'email':
        self.email = new_value
    elif attribute_change == 'note':
        self.note = new_value
    else:
        False
  @classmethod
  def find_by(cls, attribute, attribute_value):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
   for num in range(0, len(cls.contact)):
       current_contact = cls.contacts [num]
       if attribute == 'first_name' and current_contact.first_name == attribute_value:
           return current_contact
       elif attribute == 'last_name' and current_contact.last_name == attribute_value:
           return current_contact
       elif attribute == 'email' and current_contact.email == attribute_value:
           return current_contact
       elif attribute == 'note' and current_contact.note == attribute_value:
           return current_contact
       else:
           None

  @classmethod
  def delete_all(cls):
    """This method should delete all of the contacts"""


  def full_name(self):
    """Returns the full (first and last) name of the contact"""
  return self.first_name + ' ' + self.last_name

  def delete(self):
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
   Contact.contacts.remove(self)
  # Feel free to add other methods here, if you need them.
