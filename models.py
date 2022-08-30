from datetime import datetime
from extensions import db, admin
from app import app
from flask_admin.contrib.sqla import ModelView


class Card_order_model(db.Model):
    __tablename__ = 'Card_order_model'
    id = db.Column(db.Integer, primary_key = True)
    card = db.Column(db.String(50))
    currency = db.Column(db.String(50))
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    father_name = db.Column(db.String(30))
    birthday = db.Column(db.Date)
    phone_number = db.Column(db.String(13))
    address = db.Column(db.String(255))
    email = db.Column(db.String(35))

    
    def __repr__(self):
        return self.name

    def __init__(self, card, currency, name, surname, father_name, birthday, phone_number, address, email):
        self.card = card
        self.currency = currency
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.birthday = birthday
        self.phone_number = phone_number
        self.address = address
        self.email = email


    def save(self):
        db.session.add(self)
        db.session.commit()

class Plastic_card_model(db.Model):
    __tablename__ = 'Plastic_card_model'
    id = db.Column(db.Integer, primary_key = True)
    card_img = db.Column(db.String(255))
    card_name = db.Column(db.String(255))
    description = db.Column(db.Text)
    detail = db.Column(db.Text)
    price = db.Column(db.String(255), default = 'Buraxılma haqqı')
    price_v = db.Column(db.String(255))
    duration = db.Column(db.String(255), default = 'İstifadə müddəti')
    duration_v = db.Column(db.String(255))
    percent = db.Column(db.String(255), default = 'Qalıq üzrə faiz AZN')
    percent_v = db.Column(db.String(255))
    currency = db.Column(db.String(255), default = 'Valyuta')
    currency_v = db.Column(db.String(255))
    credit_line = db.Column(db.String(255), default = 'Kredit xətti')
    credit_line_v = db.Column(db.String(255))
    filter = db.Column(db.String(255))


    def __repr__(self):
        return self.card_name


    def save(self):
        db.session.add(self)
        db.session.commit()

class Campaign_model(db.Model):
    __tablename__ = 'Campaign_model'
    id = db.Column(db.Integer, primary_key = True)
    campaign_img = db.Column(db.String(255))
    campaign_name = db.Column(db.String(255))
    active_time = db.Column(db.String(255))
    description = db.Column(db.Text)
    is_individual = db.Column(db.Boolean, default = True)
    create_at = db.Column(db.DateTime, default= datetime.utcnow())


    def __repr__(self):
        return self.card_name


    def save(self):
        db.session.add(self)
        db.session.commit()

# ***************************************************************************************

class News_model(db.Model):
    __tablename__ = 'News_model'
    id = db.Column(db.Integer, primary_key = True)
    news_img = db.Column(db.String(255))
    news_name = db.Column(db.String(255))
    description = db.Column(db.Text)
    news_detail = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default= datetime.utcnow())

    def __repr__(self):
        return self.news_name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Card_extension_model(db.Model):
    __tablename__ = 'Card_extension_model'
    id = db.Column(db.Integer, primary_key = True)
    last_8 = db.Column(db.String(8))
    passport = db.Column(db.String(11))
    phone_number = db.Column(db.String(13))
    filial = db.Column(db.String(255))
    order = db.Column(db.String(255))

    def __repr__(self):
        return self.filial

    def __init__(self, last_8, passport, phone_number, filial, order):
        self.last_8 = last_8
        self.passport = passport
        self.phone_number = phone_number
        self.filial = filial
        self.order = order

    def save(self):
        db.session.add(self)
        db.session.commit()


admin.add_view(ModelView(News_model, db.session))
admin.add_view(ModelView(Card_extension_model, db.session))
admin.add_view(ModelView(Campaign_model, db.session))
admin.add_view(ModelView(Plastic_card_model, db.session))
admin.add_view(ModelView(Card_order_model, db.session))
