from django.db import models

# Create your models here.


class PeopleModel(models.Model):
    phone_number = models.CharField(
        max_length=13, unique=True, help_text="شماره موبایل"
    )
    count = models.IntegerField(help_text="تعداد")
    is_sms = models.BooleanField(help_text="ایا اس ام اس ارسال شده", default=False)
    is_recive = models.BooleanField(help_text="ایا غذا دریافت کرده", default=False)
    sms_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    recive_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    recive_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "کاربران "
        verbose_name_plural = "کاربران"


class UserModel(models.Model):
    phone_number = models.CharField(
        max_length=11, unique=True, help_text="شماره موبایل"
    )
    password = models.CharField(max_length=50, help_text="رمز عبور")
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "همکاران "
        verbose_name_plural = "همکاران"
