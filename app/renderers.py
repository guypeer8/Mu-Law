from flask import render_template
from . import *

def render_thankyou(message, status_code=200, language='en'):
    return render_template('thankyou.html',
                           langs=langs, language=language, side_menu=side_menu,
                           header=header, lang_label=lang_label, message=message
                           ), status_code

def render_page(template, data=None, on_expertise=False, language='en', description=None):
    return render_template(template,
                           on_expertise=on_expertise, langs=langs, data=data, language=language,
                           side_menu=side_menu, header=header, lang_label=lang_label, description=description)
    
def render_contact(form, title, name, email, text, submit, language='en'):
    return render_template('contact.html',
                           form=form, title=title, name=name, email=email, text=text, submit=submit,
                           langs=langs, data=contact_info, language=language, on_contact=True,
                           side_menu=side_menu, header=header, lang_label=lang_label)
