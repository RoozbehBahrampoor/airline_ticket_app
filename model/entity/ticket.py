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
        return (f"{self.id} {self.ticket_code} {self.origin} {self.destination} {self.airline}"
                f" {self.start_date_time} {self.end_date_time} {self.seat_no} {self.sold}")

    def __repr__(self):
        return (f"{self.ticket()} {self.id} id: {self.ticket_code} ticket_code:  {self.origin} origine:"
                f" {self.destination} destination: {self.airline} airline: {self.start_date_time} start_date_time:"
                f" {self.end_date_time} end_date_time: ")

    def to_tuple(self):
        return (self.id, self.ticket_code, self.origin, self.destination, self.airline, self.start_date_time,
                self.end_date_time, self.seat_no, self.sold)


    def get_id(self):
        return self.id

    def set_id(self,value):
        id_validator(value)
        self.id = value

    def get_ticket_code(self):
        return self.ticket_code

    def set_ticket_code(self, value):
        ticket_code_validator(value)
        self.ticket_code = value


    def get_origin(self):
        return self.origin

    def set_origin(self,value):
        origin_validator(value)
        self.origin = value

    def get_destination(self):
        return self.destination

    def set_destination(self, value):
        destination_validator(value)
        self.destination = value

    def get_airline(self):
        return self.airline

    def set_airline(self, value):
        airline_validator(value)
        self.airline = value

    def get_start_date_time(self):
        return self.start_date_time

    def set_start_date_time(self, value):
        start_date_time_validator(value)
        self.start_date_time = value

    def get_end_date_time(self):
        return self.end_date_time

    def set_end_date_time(self, value):
        end_date_time_validator(value)
        self.end_date_time = value

    def get_seat_no(self):
        return self.seat_no

    def set_seat_no(self, value):
        seat_no_validator(value)
        self.seat_no = value

    def get_sold(self):
        return self.sold

    def set_sold(self, value):
        sold_validator(value)
        self.sold = value






    id = property(get_id, set_id)
    ticket_code = property(get_ticket_code, set_ticket_code)
    origin = property(get_origin, set_origin)
    destination = property(get_destination, set_destination)
    airline = property(get_airline, set_airline)
    start_date_time = property(get_start_date_time, set_start_date_time)
    end_date_time = property(get_end_date_time, set_end_date_time)
    seat_no = property(get_seat_no, set_seat_no)
    sold = property(get_sold, set_sold)



