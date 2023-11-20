import re
from tinydb import TinyDB


def validate_fields(value: str) -> str:
    date_regex_n = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
    date_regex_r = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    phone_number_regex = re.compile(r'^\+?7\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}$')
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if date_regex_n.match(value) or date_regex_r.match(value):
        field_type = 'date'
        return field_type
    if phone_number_regex.match(value):
        field_type = 'phone'
        return field_type
    if email_regex.match(value):
        field_type = 'email'
        return field_type
    else:
        field_type = 'text'
        return field_type


def validate_form(form: dict) -> dict | str:
    db = TinyDB('forms_db.json')
    forms = db.all()

    for key, value in form.items():
        form[key] = validate_fields(value)

    form_for_return = {}
    form_for_return_name = ''
    for db_form in forms:
        form_for_return_act = db_form.pop('name')
        if set(db_form.items()).issubset(set(form.items())) and len(form_for_return) <= len(db_form):
            form_for_return_name = form_for_return_act
            form_for_return = db_form

    if form_for_return_name != '':
        return form_for_return_name
    else:
        return form
