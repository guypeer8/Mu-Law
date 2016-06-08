from flask import Flask, redirect, url_for
from app import *
from app.renderers import render_thankyou, render_contact, render_page
from app.forms import VisitorForm
from app.config import SECRET
from app.mail import send_email

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET

@app.route('/')
def index():
    return redirect(url_for('switch_lang', language='en'))

@app.route('/<language>')
def switch_lang(language):
    return render_page('index.html', language=language, description=description)

@app.route('/<language>/expertise')
def expertise(language):
    return render_page('expertise.html', data=legal_expertise, on_expertise=True, language=language)

@app.route('/<language>/lawyers')
def lawyers(language):
    return render_page('lawyers.html', data=lawyers_list, language=language)

@app.route('/<language>/contact', methods=['GET', 'POST'])
def contact(language):
    labels = contact_form[language]
    title = labels['title']
    name = labels['name']
    email = labels['email']
    text = labels['text']
    submit = labels['submit']
    form = VisitorForm()
    if form.validate_on_submit():
        subject = 'mu-law.com'
        body = 'Message:\n' + form.text.data
        body += '\n\nname: ' + form.name.data + '\nemail: ' + form.email.data
        send_email(subject, body)
        return redirect(url_for('thank_you', language=language))
    return render_contact(form, title, name, email, text, submit, language)

@app.route('/<language>/thank-you')
def thank_you(language):
    return render_thankyou(thanks[language], language=language)

@app.errorhandler(404)
def page_not_found(e):
    message = 'Sorry, but the page you requested was not found.'
    return render_thankyou(message, 404)

@app.errorhandler(500)
def internal_server_error(e):
    message = '<p>Sorry, the server is unable to handle your request.</p><p>Please try again in a few minutes.</p>'
    return render_thankyou(message, 500)

if __name__ == '__main__':
    app.run()
