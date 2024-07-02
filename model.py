from config import *

class Semijoia(db.Entity):
    gargantilha  = Required(str)
    pulseira = Required(str)
    brinco = Optional(str)
    def __str__(self):
        return f'{self.gargantilha}, {self.pulseira}, {self.brinco}'

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)