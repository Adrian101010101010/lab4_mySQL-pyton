"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import client_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ParcelController(GeneralController):
    """
    Realisation of Parcel controller.
    """
    _service = client_service
