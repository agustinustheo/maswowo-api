from entities.faunadb_entity import get, create, update, delete

def get_telegram_by_otp(data):
    try:
        return get('telegram_by_otp', data)
    except Exception as ex:
        raise ex

def create_telegram(data):
    try:
        return create('telegram', data)
    except Exception as ex:
        raise ex

def update_telegram(id, data):
    try:
        return update('telegram', id, data)
    except Exception as ex:
        raise ex

def delete_telegram(id):
    try:
        return delete('telegram', id)
    except Exception as ex:
        raise ex