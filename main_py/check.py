

import re

from flask_mail import Mail, Message


def check_input_dict(input_arr, stat_arr):
    if len(input_arr) != len(stat_arr):
        return False
    
    for val in input_arr:
        if val not in stat_arr:
            return False
    
    return True


# 
def check_string(format_str, stat_str):
    regular = {
        'email'     : ('^[a-z][0-9a-z.]*@[a-z]*\.[a-z]*', 128),
        'user_email': ('^[a-z][0-9a-z.]*@[a-z]*\.[a-z]*', 128),
        'password'  : ('[a-zA-Z0-9]*', 32),
        'token'     : ('[a-zA-Z0-9]*', 128),
        'name'      : ('[a-z]*', 128),
        'last_name' : ('[a-z]*', 128),
        'group_name': ('[a-z0-9]*', 32),
        'user_ball' : ('[0-9]*', 32),
        'item_name' : ('[a-z]*', 32),
        'item_id'   : ('[0-9]*', 32)
    }

    if len(format_str) > regular[stat_str][1]:
        return False

    reg = re.search(regular[stat_str][0], format_str)

    if reg is None or not reg.group() or format_str != reg.group():
        return False

    return True


def check_input_values(request_dict, stat_arr):
    to_lower = [
        'email',
        'name',
        'last_name',
        'user_email',
        'group_name',
        'item_name'
    ]

    to_integer = [
        'user_ball',
        'item_id'
    ]

    if not check_input_dict(request_dict, stat_arr):
        return (2400, None)

    user = [ ]
    for item in stat_arr:
        dict_item = request_dict[item].strip()

        if not check_string(dict_item, item):
            return (2401, None)

        if  item in to_lower:
            if item == 'name' or item == 'last_name':
                dict_item = dict_item.lower()
                dict_item = '{}{}'.format(dict_item[0].upper(), dict_item[1:len(dict_item)])
            user.append(dict_item)
        elif item in to_integer:
            dict_item = int(dict_item)
            user.append(dict_item)
        else:
            user.append(dict_item)

    return (2200, user)


def send_email(app, to_addres, token):
    subject = 'Подтверждени почты пользователя'
    sender = 'Подтверждение_почты'

    body = """
        Вы успешно прошли регистрацию в нашем приложении. Для подтверждения почты,
        Вам требуется копировать данный токе активации и использовать его в api
        запросе или вставить его в GUI форму.

        Ваш токен подтверждения: {}

        Токен является действительным 24 часа с момента регистрации аккаунта!

        Данное сообщение было создано автоматически, отвечать на него не требуется!
    """.format(token)

    code = 2202

    try:
        mail = Mail(app)
        msg = Message(subject=subject, sender=sender, recipients=[to_addres])
        msg.body = body
        mail.send(msg)
    except Exception:
        code = 2402
    
    return code