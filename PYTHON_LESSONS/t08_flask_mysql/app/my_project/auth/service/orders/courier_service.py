"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import courier_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CourierService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = courier_dao
