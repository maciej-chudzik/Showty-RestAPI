from marshmallow import post_load

from ma import ma
from models.like import LikeModel


class LikeSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = LikeModel
        dump_only = ("login",)
        exclude = ("likes_id",)
        load_instance = True
