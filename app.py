from flask import Flask, render_template, request
import requests, xmltodict
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bank123@127.0.0.1:3306/bank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['FLASK_ADMIN_SWATCH'] = 'yeti'

from extensions import *
from models import *
from form_models import *


if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    app.run(port=5000, debug=True)


@app.route("/card_order/", methods=['GET', 'POST'])
def card_order():
    post_data = request.form
    form = Card_order_form()
    print('asd')
    if request.method == 'POST':
        print('post')
        form=Card_order_form(data=post_data)
        if form.validate_on_submit():
            print('val')
            card_order = Card_order_model(card = form.card.data , currency = form.currency.data, name = form.name.data, surname = form.surname.data, father_name = form.father_name.data, birthday = form.birthday.data, phone_number = form.phone_number.data, address = form.address.data, email = form.email.data)
            card_order.save()
    return render_template('card_order.html', form = form)


@app.route("/campaign/")
def campaign():
    r = Campaign_model.query.all()
    return render_template('campaign.html', campaigns = r)


@app.route('/header/')
def header():
    return render_template('base.html')


@app.route('/plastic_card/')
def plastic_card():
    r = Plastic_card_model().query.all()
    return render_template('plastic_cards.html', cards = r)

# *****************************************************************************************

@app.route('/plastic_card/<int:id>')
def card_detail(id):
    r = Plastic_card_model.query.filter(Plastic_card_model.id==id).first()
    return render_template('card_detail.html', card = r)


@app.route('/news/')
def news():
    r = News_model.query.all()
    return render_template('news.html', news_ = r)

@app.route('/news/<int:id>')
def news_detail(id):
    r = News_model.query.filter(News_model.id == id).first()
    return render_template('news_detail.html', news = r)


@app.route("/card_extension/", methods=['GET', 'POST'])
def card_extension():
    post_data = request.form
    form = Card_extension_form()
    print('asd')
    if request.method == 'POST':
        print('post')
        form=Card_extension_form(data=post_data)
        if form.validate_on_submit():
            print('val')
            card_extension = Card_extension_model(last_8 = form.last_8.data , passport = form.passport.data, phone_number = form.phone_number.data, filial = form.filial.data, order = form.order.data)
            card_extension.save()
    return render_template('card_extension.html', form = form)


@app.route('/')
def homepage():
    m = requests.get(f'https://www.cbar.az/currencies/{datetime.now().strftime("%d.%m.%Y")}.xml')
    m_dict = xmltodict.parse(m.content)
    r = News_model.query.all()
    k = Campaign_model.query.all()
    return render_template('Esas_Sehife.html', currency = m_dict, news = r, campaigns = k, show=False)