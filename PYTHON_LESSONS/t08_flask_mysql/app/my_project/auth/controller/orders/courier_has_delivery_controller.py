"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import client_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CourierHasDeliveryController(GeneralController):
    """
    Realisation of CourierHasDelivery controller.
    """
    _service = client_service
