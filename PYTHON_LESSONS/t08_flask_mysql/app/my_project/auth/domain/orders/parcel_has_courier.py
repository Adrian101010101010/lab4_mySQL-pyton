"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ParcelHasCourier(db.Model):
    """
    Model declaration for the relationship table between Parcel and Courier.
    """
    __tablename__ = "parcel_has_courier"

    courier_id = db.Column(db.BigInteger, db.ForeignKey('courier.id'), primary_key=True)
    parcel_id = db.Column(db.BigInteger, db.ForeignKey('parcel.id'), primary_key=True)

    def __repr__(self) -> str:
        return f"ParcelHasCourier({self.courier_id}, {self.parcel_id})"
