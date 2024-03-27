import random

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_mail import Message
from sqlalchemy import func

from app.models.models import Event, Views
from app.utils import mail

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@index_bp.route('/home')
def index():
    random_events = Event.query.order_by(func.random()).limit(3).all()
    random_view = Views.query.order_by(func.random()).first()
    return render_template('index.html', random_events=random_events, random_view=random_view)


@index_bp.route('/about')
def about():
    return render_template('about.html')


@index_bp.route('/whatwedo')
def whatwedo():
    return render_template('whatwedo.html')


@index_bp.route('/donations')
def donations():
    return render_template('donations.html')


@index_bp.route('/donate')
def donate():
    return render_template('donate.html')


@index_bp.route('/events')
def events():
    all_events = Event.query.all()
    return render_template('events.html', all_events=all_events)


@index_bp.route('/writeus', methods=['GET', 'POST'])
def writeus():
    if request.method == 'POST':
        customer_name = request.form.get('customerName')
        customer_email = request.form.get('customerEmail')
        customer_company = request.form.get('customerCompany')
        customer_note = request.form.get('customerNote')
        spam_protection = request.form.get('spamProtection')

        if spam_protection.lower() != 'ten':
            flash('Please check the spam protection box', category='error')
            return redirect(url_for('index.writeus'))

        msg = Message('New message from your website', sender='your-email@example.com',
                      recipients=['your-email@example.com'])
        msg.body = f'''From: {customer_name} <{customer_email}>
        Company: {customer_company}
        Message: {customer_note}'''

        try:
            mail.send(msg)
        except Exception as e:
            print(e)
            flash('Something went wrong, please try again', category='error')
            return redirect(url_for('index.writeus'))

        flash('Thank you for your message!', category='success')
        return redirect(url_for('index.writeus'))

    return render_template('writeus.html')


@index_bp.route('/comments')
def comments():
    all_views = Views.query.all()
    return render_template('comments.html', all_views=all_views)
