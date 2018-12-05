import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    自己继承了 User 方便以后字段扩展
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'user'
