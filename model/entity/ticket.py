from model.tools.validation import *

class ticket:
    def __init__(self,id ,ticket_code ,origin ,destination ,airline ,start_date_time ,end_date_time ,seat_no ,sold ):
        self.id = id
        self.ticket_code = ticket_code 
        self.origin = origin 
        self.destination = destination 
        self.airline = airline
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.seat_no = seat_no
        self.sold = sold

    def ticket(self):
        return f"{self.id} {self.ticket_code}"

    def __repr__(self):
        return f"{self.ticket()} {self.origin}"

    def to_tuple(self):
        return (self.id, self.ticket_code, self.origin)


    def get_id(self):
        return self.id

    def set_ticket_code(self, value):
        ticket_code_validator(value)
        self.ticket_code = value


    def get_origin(self):
        return self.origin

    def set_family(self, value):
        destination_validator(value)
        self.destination = value

    def get_airline(self):
        return self.airline

    def set_airline(self, value):
        airline_validator(value)
        self.airline = value

    def get_start_date_time(self):
        get_start_date_time_validator(value)
        self.start_date_time = value


    name = property(get_name, set_name)
    family = property(get_family, set_family)
    age = property(get_age, set_age)

