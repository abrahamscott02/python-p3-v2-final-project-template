from models.__init__ import CURSOR, CONN

class Coach:
    all = {}

    def __init__(self, name, years_experience, id=None):
        self.id = id
        self.name = name
        self.years_experience = years_experience

    def __repr__(self):
        return f"<Coach {self.id}: {self.name}, {self.years_experience} years experience>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name.strip()
        else:
            raise ValueError("Name cannot be an empty string")

    @property
    def years_experience(self):
        return self._years_experience

    @years_experience.setter
    def years_experience(self, years_experience):
        if isinstance(years_experience, int) and years_experience >= 0:
            self._years_experience = years_experience
        else:
            raise ValueError("Experience years must be a non-negative integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS coaches (
                id INTEGER PRIMARY KEY,
                name TEXT,
                years_experience INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, years_experience):
        sql = """ INSERT INTO coaches (name, years_experience) VALUES (?, ?) """
        CURSOR.execute(sql, (name, years_experience))
        CONN.commit()
        return cls(name, years_experience, CURSOR.lastrowid)

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM coaches"
        rows = CURSOR.execute(sql).fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]  # id is the last argument here

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM coaches WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    def update(self):
        sql = "UPDATE coaches SET name = ?, years_experience = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.years_experience, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM coaches WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def athletes(self):
        from models.athlete import Athlete
        return Athlete.find_by_coach(self.id)
