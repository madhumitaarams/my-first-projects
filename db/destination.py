class Destination:
    def __init__(self, destination_id=None, name=None, description=None, price=None):
        self.destination_id = destination_id
        self.name = name
        self.description = description
        self.price = price

    @staticmethod
    def add_destination(name, description, price):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO destinations (name, description, price) VALUES (%s, %s, %s)", 
                       (name, description, price))
        conn.commit()
        conn.close()
        print(f"Destination '{name}' added successfully!")

    @staticmethod
    def view_destinations():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM destinations")
        destinations = cursor.fetchall()
        conn.close()
        return destinations

    @staticmethod
    def delete_destination(destination_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM destinations WHERE destination_id = %s", (destination_id,))
        conn.commit()
        conn.close()
        print("Destination deleted successfully!")
