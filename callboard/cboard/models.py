from django.db import models
from django.contrib.auth.models import User

tank = "TN"
heal = "HL"
dd = "DD"
wendor = "WN"
guildmaster = "GM"
questgiver = "QG"
blacksmith = "BM"
leatherworker = "LW"
alchemyst = "AL"
spellmaster = "SM"

CATEGORY = [
    (tank, "Танк"),
    (heal, "Хил"),
    (dd, "ДД"),
    (wendor, "Торговец"),
    (guildmaster, "Гильдмастер"),
    (questgiver, "Квестгивер"),
    (blacksmith, "Кузнец"),
    (leatherworker, "Кожевник"),
    (alchemyst, "Зельевр"),
    (spellmaster,"Мастер заклинаний"),
]

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True,)

class PostCategory(models.Model): #категория объявления
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model): #комментарий
    pass