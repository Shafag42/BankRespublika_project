from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, RadioField
from wtforms.validators import DataRequired, Length, Email


class Card_order_form(FlaskForm):
    card = SelectField(label='Kartı əlavə et', choices=[('NeoKart Standard', 'NeoKart Standard'), ('NeoKart Premium', 'NeoKart Premium'), ('Mover Visa Platinium', 'Mover Visa Platinium'), ('Mover Visa Classic','Mover Visa Classic'), ('MasterCard Debet','MasterCard Debet'), ('MasterCard Platinum - Cümhuriyyət 100 il.','MasterCard Platinum - Cümhuriyyət 100 il.'), ('Visa Virtual','Visa Virtual'), ('VISA Gold','VISA Gold'), ('MasterCard Gold','MasterCard Gold'), ('VISA Classic','VISA Classic'), ('MasterCard Standard','MasterCard Standard')])
    currency = SelectField(label='Kartın valyutasını seç', choices=[('AZN', 'AZN'), ('ABS dollari', 'ABŞ dolları'), ('Avro', 'Avro')])
    name = StringField(label = 'Adınız', validators=[DataRequired(), Length(min=3, max=30)])
    surname = StringField(label = 'Soyadınız', validators=[DataRequired(), Length(min=3, max=30)])
    father_name = StringField(label = 'Ata adınız', validators=[DataRequired(), Length(min=3, max=30)])
    birthday = DateField(label = 'Doğum tarixi', format='%Y-%m-%d',validators=[DataRequired()])
    phone_number = StringField(label = 'Mobil nömrəniz', validators=[DataRequired(), Length(max=13)])
    address = StringField(label = 'Qeydiyyat ünvanınız', validators=[DataRequired()])
    email = StringField(label = 'Email', validators=[DataRequired(), Email(), Length(max=35)])

class Card_extension_form(FlaskForm):
    last_8 = StringField(label = 'Kartın son 8 rəqəmi:', validators = [DataRequired(), Length(min = 8, max = 8)])
    passport = StringField(label = 'Şəxsiyyəti təsdiq edən sənəd:', validators = [DataRequired(), Length(max = 11)])
    phone_number = StringField(label = 'Mobil nömrəniz', validators=[DataRequired(), Length(max=13)])
    filial = SelectField(label='Kart götürüləcək filial', choices=[('Xırdalan Filialı', 'Xırdalan Filialı'), ('Gəncə filialı', 'Gəncə filialı'), ('Mingəçevir filialı', 'Mingəçevir filialı'), ('Yevlax filialı', 'Yevlax filialı'), ('Bərdə filialı', 'Bərdə filialı'), ('Zaqatala filialı', 'Zaqatala filialı'), ('Şirvan filialı', 'Şirvan filialı'), ('Sabirabad filialı', 'Sabirabad filialı'), ('Quba filialı', 'Quba filialı'), ('Qax filialı', 'Qax filialı'), ('Masallı fililalı', 'Masallı fililalı'), ('Lənkəran filialı', 'Lənkəran filialı'), ('Abşeron şöbəsi', 'Abşeron şöbəsi'), ('Xaçmaz filialı', 'Xaçmaz filialı'), ('Baş Ofis', 'Baş Ofis'), ('Yasamal Filialı', 'Yasamal Filialı'), ('Neftçilər filialı', 'Neftçilər filialı'), ('Nəsimi filialı', 'Nəsimi filialı'), ('Nizami filialı', 'Nizami filialı'), ('Memar Əcəmi filialı', 'Memar Əcəmi filialı'), ('Bakıxanov filialı', 'Bakıxanov filialı'), ('Əhmədli filialı', 'Əhmədli filialı'), ('Ağa Neymətulla şöbəsi', 'Ağa Neymətulla şöbəsi'), ('Azneft filialı / Ofis24', 'Azneft filialı / Ofis24'), ('Azadlıq filialı', 'Azadlıq filialı'), ('Cəlilabad filialı', 'Cəlilabad filialı')])
    order = RadioField(label = 'Sifariş növü', choices=[('10 azn', '1 gün / 10 azn'),('3 gün', '3 gün / 0 azn')], default = '10 azn')
