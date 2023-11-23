"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import parcel_has_courier_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ParcelHasCourierService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = parcel_has_courier_dao
