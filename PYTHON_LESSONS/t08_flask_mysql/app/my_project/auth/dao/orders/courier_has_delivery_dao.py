"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import CourierHasDelivery


class CourierHasDeliveryDAO(GeneralDAO):
    """
    Realisation of CourierHasDelivery data access layer.
    """
    _domain_type = CourierHasDelivery

    def find_by_courier_id(self, courier_id: int) -> List[object]:
        """
        Gets CourierHasDelivery objects from the database table by field 'courier_id'.
        :param courier_id: courier_id value
        :return: search objects
        """
        return self._session.query(CourierHasDelivery).filter(CourierHasDelivery.courier_id == courier_id).all()

    def find_by_delivery_id(self, delivery_id: int) -> List[object]:
        """
        Gets CourierHasDelivery objects from the database table by field 'delivery_id'.
        :param delivery_id: delivery_id value
        :return: search objects
        """
        return self._session.query(CourierHasDelivery).filter(CourierHasDelivery.delivery_id == delivery_id).all()
