class Booking:
    def __init__(self, booking_id=None, user_id=None, destination_id=None, date_of_travel=None):
        self.booking_id = booking_id
        self.user_id = user_id
        self.destination_id = destination_id
        self.date_of_travel = date_of_travel

    @staticmethod
    def make_booking(user_id, destination_id, date_of_travel):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bookings (user_id, destination_id, date_of_travel) VALUES (%s, %s, %s)", 
                       (user_id, destination_id, date_of_travel))
        conn.commit()
        conn.close()
        print("Booking confirmed!")

    @staticmethod
    def view_bookings(user_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT b.booking_id, d.name, b.date_of_travel FROM bookings b JOIN destinations d ON b.destination_id = d.destination_id WHERE b.user_id = %s", (user_id,))
        bookings = cursor.fetchall()
        conn.close()
        return bookings
