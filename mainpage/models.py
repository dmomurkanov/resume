from django.db import models
from ckeditor.fields import RichTextField


class PersonalInfo(models.Model):
    fullname = models.CharField("Полное имя", max_length=255)
    email = models.CharField("Почта", max_length=255, default="")
    phone_number = models.CharField("Номер телефона", max_length=255, default="")
    linked_in = models.CharField("Ссылка на LinkedIn", max_length=255, default="")
    github = models.CharField("Ссылка на GitHub", max_length=255, default="")
    profession = models.CharField("Профессия", max_length=255)
    resume_file = models.FileField("Файл резюме", upload_to="perosnal")
    about_me = RichTextField("Текст обо мне")
    image = models.ImageField("Картинка баннера", upload_to="personal", null=True)
    image_mobile = models.ImageField("Картинка баннера для мобилки", upload_to="personal", null=True)

    class Meta:
        verbose_name = "Персональная информальная"
        verbose_name_plural = "Персональная информация"

    def __str__(self):
        return self.fullname