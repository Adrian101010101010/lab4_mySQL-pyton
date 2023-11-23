"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import operator_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class OperatorController(GeneralController):
    """
    Realisation of Operator controller.
    """
    _service = operator_service
