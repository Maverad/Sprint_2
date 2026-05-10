class EmployeeSalary:
        hourly_payment = 400

        def __init__(self, name=None, hours=None, rest_days=0, email=None):
            self.name = name
            self.hours = hours
            self.rest_days = rest_days
            self.email = email

        def get_hours(self) -> int:
            if self.hours is None:
                return (7 - self.rest_days) * 8
            else:
                return self.hours
        
        def get_email(self) -> str:
            if self.email is None:
                self.email = f'{self.name}@email.com'
                return self.email
            else:
                return self.email
            
        @classmethod
        def set_hourly_payment(cls, new_value:int) -> None:
            cls.hourly_payment = new_value

        def salary(self) -> int:
            return self.hourly_payment * self.get_hours()
        