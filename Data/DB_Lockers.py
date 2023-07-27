from peewee import *
import datetime
from datetime import date

db = SqliteDatabase('Lockers.db')

class BaseModel(Model):
    class Meta:
        database = db

class Locker(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=5)
    status = CharField(max_length=25)
    spare_key = BooleanField(default=True)
    comment = TextField()
    rental_counter = CharField(default=0)
    created_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        order_by = ('name',)

class Tenant(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField()
    locker = ForeignKeyField(Locker, related_name='tenants')
    number = CharField()
    end_date_of_the_lease = DateTimeField()

class History(BaseModel):
    id = PrimaryKeyField(null=False)
    comment = TextField()
    locker = ForeignKeyField(Locker, related_name='payments')
    key = BooleanField(default=True)
    tenant = ForeignKeyField(Tenant, related_name='payments')
    number = CharField()
    created_at = DateTimeField(default=datetime.datetime.now())
    srock = TextField()
    summ = CharField(max_length=12)
    end_date_of_the_lease = DateTimeField()

def create_lockers():
    btns = {
        'btn': 'Шкафчик №1', 'btn2': 'Шкафчик №2', 'btn3': 'Шкафчик №3', 'btn4': 'Шкафчик №4',
        'btn5': 'Шкафчик №5', 'btn6': 'Шкафчик №6', 'btn7': 'Шкафчик №7', 'btn8': 'Шкафчик №8',
        'btn9': 'Шкафчик №9', 'btn10': 'Шкафчик №10', 'btn11': 'Шкафчик №11', 'btn12': 'Шкафчик №12',
        'btn13': 'Шкафчик №13', 'btn14': 'Шкафчик №14', 'btn15': 'Шкафчик №15', 'btn16': 'Шкафчик №16',
        'btn17': 'Шкафчик №17', 'btn18': 'Шкафчик №18', 'btn19': 'Шкафчик №19', 'btn20': 'Шкафчик №20',
        'btn21': 'Шкафчик №21', 'btn22': 'Шкафчик №22', 'btn23': 'Шкафчик №23', 'btn24': 'Шкафчик №24',
        'btn25': 'Шкафчик №25', 'btn26': 'Шкафчик №26', 'btn27': 'Шкафчик №27', 'btn28': 'Шкафчик №28',
        'btn29': 'Шкафчик №29', 'btn30': 'Шкафчик №30', 'btn31': 'Шкафчик №31', 'btn32': 'Шкафчик №32',
        'btn33': 'Шкафчик №33', 'btn34': 'Шкафчик №34', 'btn35': 'Шкафчик №35', 'btn36': 'Шкафчик №36',
        'btn37': 'Шкафчик №37', 'btn38': 'Шкафчик №38', 'btn39': 'Шкафчик №39', 'btn40': 'Шкафчик №40',
        'btn41': 'Шкафчик №41', 'btn42': 'Шкафчик №42', 'btn43': 'Шкафчик №43', 'btn44': 'Шкафчик №44',
        'btn45': 'Шкафчик №45', 'btn46': 'Шкафчик №46', 'btn47': 'Шкафчик №47', 'btn48': 'Шкафчик №48',
        'btn49': 'Шкафчик №49', 'btn50': 'Шкафчик №50', 'btn51': 'Шкафчик №51', 'btn52': 'Шкафчик №52',
        'btn53': 'Шкафчик №53', 'btn54': 'Шкафчик №54', 'btn55': 'Шкафчик №55', 'btn56': 'Шкафчик №56',
        'btn57': 'Шкафчик №57', 'btn58': 'Шкафчик №58', 'btn59': 'Шкафчик №59', 'btn60': 'Шкафчик №60'
    }

    with db.atomic():
        for btn, name in btns.items():
            Locker.create(name=name, status='Пуст', comment='Пуст')

if not db.table_exists('locker'):
    db.connect()
    db.create_tables([Locker, Tenant, History])
    create_lockers()
else:
    db.connect()
