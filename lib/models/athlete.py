from models.__init__ import CURSOR, CONN
from models.coach import Coach

class Athlete:
    all = {}

    def __init__(self, name, sport, coach_id, id=None):
        self.id = id
        self.name = name
        self.sport = sport
        self.coach_id = coach_id

    def __repr__(self):
        return f"<Athlete {self.id}: {self.name}, Sport: {self.sport}, Coach ID: {self.coach_id}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name.strip()
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def sport(self):
        return self._sport

    @sport.setter
    def sport(self, sport):
        if isinstance(sport, str) and sport.strip():
            self._sport = sport.strip()
        else:
            raise ValueError("Sport must be a non-empty string")

    @property
    def coach_id(self):
        return self._coach_id

    @coach_id.setter
    def coach_id(self, coach_id):
        # Validate that the coach_id is a valid reference to an existing coach
        if isinstance(coach_id, int) and Coach.find_by_id(coach_id):
            self._coach_id = coach_id
        else:
            raise ValueError("Coach ID must reference a valid coach")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS athletes (
                id INTEGER PRIMARY KEY,
                name TEXT,
                sport TEXT,
                coach_id INTEGER,
                FOREIGN KEY (coach_id) REFERENCES coaches(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, sport, coach_id):
        sql = "INSERT INTO athletes (name, sport, coach_id) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.name, self.sport, self.coach_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        # return cls(name, sport, coach_id, CURSOR.lastrowid)

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM athletes"
        rows = CURSOR.execute(sql).fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]  # id is the last argument here

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM athletes WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    @classmethod
    def find_by_coach(cls, coach_id):
        sql = "SELECT * FROM athletes WHERE coach_id = ?"
        rows = CURSOR.execute(sql, (coach_id,)).fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]  # id is the last argument here

    def update(self):
        sql = "UPDATE athletes SET name = ?, sport = ?, coach_id = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.sport, self.coach_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM athletes WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
