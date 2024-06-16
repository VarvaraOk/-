# Варвара Оконечникова, 17-я когорта, финальный проект. Инженер по тестированию плюс.

import sender_stand_request
import data

def create_order():
    current_body = data.order_body.copy()
    current_body ["firstName"] = "Naruto"
    track_number = sender_stand_request.post_new_order(current_body)
    return str(track_number.json()["track"])

def positive_assert():
    track_number = create_order()
    current_params = data.params_get.copy()
    current_params["t"] = track_number
    response = sender_stand_request.get_order(current_params)
    assert response.status_code == 200

def test_order():
    positive_assert()
