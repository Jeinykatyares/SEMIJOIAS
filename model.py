from config import *

class Semijoia(db.Entity):
    codigo  = Required(str)
    valor = Required(str)
    desc=Required(str)
    cor= Required(str)
    qualidade=Required(str)
    def __str__(self):
        return f'{self.codigo}, {self.valor}, {self.desc}', {self.cor}, {self.qualidade}

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)