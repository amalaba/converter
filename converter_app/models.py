from converter_app import converter_db

ROLE_USER=0
ROLE_ADMIN=1

class Convert_details(converter_db.Model):

    id=converter_db.Column(converter_db.Integer, primary_key=True, autoincrement=True)
    convert_attr=converter_db.Column(converter_db.String(50)),
    from_attr=converter_db.Column(converter_db.String(50)),
    to_attr=converter_db.Column(converter_db.String(50)),
    multiplication_factor=converter_db.Column(converter_db.Double(50)),

def __repr__(self):
    return 'Conversion on %r' %(self.convert_attr)

