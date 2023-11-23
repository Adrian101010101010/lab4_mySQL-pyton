"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Courier

class CourierDAO(GeneralDAO):
    """
    Realisation of Courier data access layer.
    """
    _domain_type = Courier

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Courier objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Courier).filter(Courier.name == name).order_by(Courier.name).all()

    def find_by_surname(self, surname: str) -> List[object]:
        """
        Gets Courier objects from the database table by field 'surname'.
        :param surname: surname value
        :return: search objects
        """
        return self._session.query(Courier).filter(Courier.surname == surname).order_by(Courier.surname).all()

    def find_by_phone(self, phone: str) -> List[object]:
        """
        Gets Courier objects from the database table by field 'phone'.
        :param phone: phone value
        :return: search objects
        """
        return self._session.query(Courier).filter(Courier.phone == phone).order_by(Courier.phone).all()
