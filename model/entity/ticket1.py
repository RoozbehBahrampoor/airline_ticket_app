from model.tools.validation import *


class Person:
    def __init__(self, id, ticket_code, origin, destination, airline, start_date_time, end_date_time, seat_no, sold):
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
        return f"{self.id} {self.ticket_code} {self.origin} {self.destination} {self.airline} {self.start_date_time} {self.end_date_time} {self.seat_no} {self.sold}"

    def __repr__(self):
        return f"{self.ticket()} {self.id} id: {self.ticket_code} ticket_code: {self.origin} origin: {self.destination} destination: {self.airline} airline: {self.start_date_time} start_date_time:"

    def to_tuple(self):
        return (self.id, self.ticket_code, self.origin, self.destination, self.airline, self.start_date_time, self.end_date_time, self.seat_no, self.sold)

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        id_validator(value)
        self.id = value

    @property
    def ticket_code(self):
        return self.ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        ticket_code_validator(value)
        self.ticket_code = value

    @property
    def origin(self):
        return self.origin

    @origin.setter
    def origin(self, value):
        origin_validator(value)
        self.origin = value

    @property
    def destination(self):
        return self.destination


    @destination.setter
    def destination(self, value):
        destination_validator(value)
        self.destination = value

    @property
    def airline(self):
        return self.airline

    @airline.setter
    def airline(self, value):
        airline_validator(value)
        self.airline = value

    @property
    def start_date_time(self):
        return self.start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        start_date_time_validator(value)
        self.start_date_time = value

    @property
    def end_date_time(self):
        return self.end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        end_date_time_validator(value)
        self.end_date_time = value

    @property
    def seat_no(self):
        return self.seat_no

    @seat_no.setter
    def seat_no(self, value):
        seat_no_validator(value)
        self.seat_no = value

    @property
    def sold(self):
        return self.sold

    @sold.setter
    def sold(self, value):
        sold_validator(value)



