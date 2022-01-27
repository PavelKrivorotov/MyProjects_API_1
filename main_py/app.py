

import secrets

from flask import Flask, request
from werkzeug import security

from models import OAuth, User
from check import check_input_values, send_email


app = Flask(__name__)
app.debug = True
app.secret_key = 'NWIHQ03YR7TDCYGBO22TE1P928F0UI'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_DEFAULT_SENDER'] = ''
app.config['MAIL_PASSWORD'] = ''



@app.route('/api/oautch/registration', methods=['POST'])
def registration():
    user_stat = ['email', 'password', 'name', 'last_name']

    args = request.form.to_dict()
    # print(args)

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    # Создаем хеш пароля
    hash_pass = security.generate_password_hash(data[1])
    data[1] = hash_pass

    # Создаём токен активации
    token_activation = secrets.token_hex(64)
    data.append(token_activation)

    # Выполняем запрос к базе данныx
    status = OAuth.registration(params=data)

    if status != 1201:
        return {'ststus':'True', 'code':status}

    # Отправляем письмо с токеном на почту
    code = send_email(app, data[0], token_activation)

    if code != 2202:
        return {'ststus':'True', 'code':code}

    return {'ststus':'True', 'code':status}


@app.route('/api/oautch/authentication', methods=['POST'])
def authentication():

    user_stat = ['email', 'token']

    args = request.form.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}
    
    # 
    token = secrets.token_hex(64)
    data.append(token)

    # 
    status = OAuth.authentication(params=data)

    return {'status':'True', 'code':status, 'token':token}


@app.route('/api/oautch/authorisation', methods=['POST'])
def authorisation():

    user_stat = ['email', 'password']

    args = request.form.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}
    
    # Проверяем корректность введённого пароля
    hash_pass = OAuth.check_password(params=data[0])

    # Проверяем статус-код, который вернула БД и сверяем пароль
    if hash_pass[0] != 1204 or ( not security.check_password_hash(hash_pass[1], data[1]) ):
        return {'status':'False', 'code':'Not correct password!'}
    
    # Создаём новый токен доступа
    token = secrets.token_hex(64)

    # Обращаемся к БД
    status = OAuth.authorisation(params=[data[0], token])

    return {'status':'True', 'code':status, 'token':token}


@app.route('/api/oautch/delete', methods=['POST'])
def delete_user():

    user_stat = ['email', 'password']

    args = request.form.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    # Отправляем запрос в БД и вытаскиваем хешированный пароль,
    # которому соответствует введённый email.
    hash_pass = OAuth.check_password(params=data[0])

    # Проверяем корректность пароля
    if hash_pass[0] != 1204 or ( not security.check_password_hash(hash_pass[1], data[1]) ):
        return {'status':'False', 'code':'Not correct password!'}

    # Обращаемся в БД для выполнения операции удаления пользователя
    status = OAuth.delete_user(params=data[0])

    return {'status':'True', 'code':status}




@app.route('/api/logic/create-group', methods=['GET'])
def create_group():
    user_stat = ['email', 'token', 'group_name']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}
    
    status = User.create_group(params=data)

    return {'status':'True', 'code':status}


@app.route('/api/logic/delete-group', methods=['GET'])
def delete_group():
    user_stat = ['email', 'token']

    args = request.args.to_dict()

    code, data  = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    status = User.delete_group(params=data)

    return {'status':'True', 'code':status}


@app.route('/api/logic/add-user', methods=['GET'])
def add_user_in_group():
    user_stat = ['email', 'token', 'user_email']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}
    
    status = User.add_user(params=data)

    return {'status':'True', 'code':status}


@app.route('/api/logic/drop-user', methods=['GET'])
def drop_user_in_group():
    user_stat = ['email', 'token', 'user_email']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    status = User.delete_user(params=data)

    return {'status':'True', 'code':status}


@app.route('/api/logic/add-item', methods=['GET'])
def add_item_in_group():
    user_stat = ['email', 'token', 'item_name']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    status = User.add_item(params=data)

    return {'status':'True', 'code':status}


@app.route('/api/logic/drop-item', methods=['GET'])
def drop_item_in_group():
    user_stat = ['email', 'token', 'item_name']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    status = User.delete_item(params=data)

    return {'status':'True', 'code':status}


@app.route('/api/logic/update-users-group-data', methods=['GET'])
def update_data_in_group():
    user_stat = ['email', 'token', 'user_email', 'user_ball', 'item_id']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    status = User.update_data(params=data)

    return {'status':'True', 'code':status}


@app.route('/api/logic/search-group-items', methods=['GET'])
def search_items_in_group():
    user_stat = ['email', 'token']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}
    
    answ_data = User.select_items(params=data)

    out = {

    }
    for index in range(len(answ_data)):
        out[index + 1] = {
            'item_id'   : answ_data[index][0],
            'item_name' : answ_data[index][1]
        }
    
    return {'status':'True', 'data':out}


@app.route('/api/logic/search-group-ball', methods=['GET'])
def search_data_in_group():
    user_stat = ['email', 'token', 'item_id']

    args = request.args.to_dict()

    code, data = check_input_values(args, user_stat)

    if code != 2200:
        return {'status':'False', 'code':code}

    answ_data = User.select_data(params=data)

    out = {

    }
    for index in range(len(answ_data)):
        out[index + 1] = {
            'id'        : answ_data[index][0],
            'name'      : answ_data[index][1],
            'last_name' : answ_data[index][2],
            'ball'      : answ_data[index][3]
        }

    return {'status':'True', 'data':out}


if __name__ == '__main__':
    app.run()