
import sqlalchemy as sa
from sqlalchemy import orm

from .database import SqlAlchemyBase


class Battle(SqlAlchemyBase):
    __tablename__ = 'battles'

    id = sa.Column(sa.Integer,primary_key=True, autoincrement=True)

    offer_id = sa.Column(sa.Integer, sa.ForeignKey("offers.id"))

    offer = orm.relationship("Offer")

    accept_id = sa.Column(sa.Integer, sa.ForeignKey("accepts.id"))
    accept = orm.relationship("Accept")

    # first_player_id = sa.Column(sa.Integer, sa.ForeignKey("offers.user_id"))
    # second_player_id = sa.Column(sa.Integer, sa.ForeignKey("accepts.user_id"))

    log =  orm.relationship("Round", back_populates='battle')

