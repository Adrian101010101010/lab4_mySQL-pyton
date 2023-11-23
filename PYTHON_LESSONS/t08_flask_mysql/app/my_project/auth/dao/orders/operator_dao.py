"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Operator


class OperatorDAO(GeneralDAO):
    """
    Realisation of Operator data access layer.
    """
    _domain_type = Operator

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Operator objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Operator).filter(Operator.name == name).order_by(Operator.name).all()

    def find_by_surname(self, surname: str) -> List[object]:
        """
        Gets Operator objects from the database table by field 'surname'.
        :param surname: surname value
        :return: search objects
        """
        return self._session.query(Operator).filter(Operator.surname == surname).order_by(Operator.surname).all()

    def find_by_phone(self, phone: str) -> List[object]:
        """
        Gets Operator objects from the database table by field 'phone'.
        :param phone: phone value
        :return: search objects
        """
        return self._session.query(Operator).filter(Operator.phone == phone).order_by(Operator.phone).all()
