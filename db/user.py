class User:
    def __init__(self, user_id=None, name=None, email=None, password=None, role='user'):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def register(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)", 
                       (self.name, self.email, self.password, self.role))
        conn.commit()
        conn.close()
        print("User registered successfully!")

    @staticmethod
    def login(email, password):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            print(f"Welcome {user[1]}!")
            return User(user_id=user[0], name=user[1], email=user[2], role=user[4])
        else:
            print("Invalid login credentials!")
            return None
