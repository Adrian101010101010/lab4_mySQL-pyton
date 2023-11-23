"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import courier_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CourierController(GeneralController):
    """
    Realisation of Courier controller.
    """
    _service = courier_service
