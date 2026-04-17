import uuid

class Customer:
    def __init__(self, name, email, phone, customer_id= None):
        self.id = customer_id if customer_id else str(uuid.uuid4())[:8]
        self._name = name.strip().title()
        self._email = email.strip().title()
        self._phone = phone.strip()
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone(self):
        return self._phone
    
    @name.setter
    def name(self, value):
        self._name = value

    @email.setter
    def email(self, value):
        self._email = value

    @phone.setter
    def phone(self, value):
        self._phone = value

    def to_dict(self):
        return{
            "id": self.id,
            "name": self._name,
            "email": self._email,
            "phone": self._phone
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data["name"], 
            email = data["email"], 
            phone = data["phone"], 
            customer_id = data["id"]
        )
    
    def __str__(self):
        return (
            f"[{self.id}] {self._name} | "
            f"Email: {self._email} | Telefone: {self._phone}"
        )