class EmployeeSalary:
        hourly_payment = 400

        def __init__(self, name=None, hours=None, rest_days=0, email=None):
            self.name = name
            self.hours = hours
            self.rest_days = rest_days
            self.email = email

        @classmethod
        def get_hours(cls, name=None, hours=None, rest_days=0, email=None):
            if hours is None:
                hours = (7 - rest_days) * 8
            return cls(name, hours, rest_days, email)
        
        @classmethod
        def get_email(cls, name=None, hours=None, rest_days=0, email=None):
            if email is None:
                email = f'{name}@email.com'
            return cls.get_hours(name, hours, rest_days, email)
            
        @classmethod
        def set_hourly_payment(cls, new_value:int) -> None:
            cls.hourly_payment = new_value

        def salary(self) -> int:
            return self.hourly_payment * self.hours
        
x = EmployeeSalary.get_email()
print(x.email)