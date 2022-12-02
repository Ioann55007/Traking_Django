from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Alog(models.Model):
    fery = models.AutoField(primary_key=True)
    arry = models.CharField(max_length=110)
    date = models.DateField(auto_now=True)
    vdate = models.DateField(auto_now_add=True)
    gdate = models.DateTimeField(auto_now=True)
    cdate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eemail = models.EmailField()
    feld_field = models.DurationField()
    file = models.FileField(upload_to='')


class Logo(models.Model):
    id = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, primary_key=True)
    slug = models.SlugField()
    imy_name = models.CharField(max_length=80)
    ip_new = models.TextField()
    file_path = models.UUIDField()
    url = models.URLField()


class Class(models.Model):
    add_class = models.CharField(max_length=99)


def get_deleted_user_instance():
    return User.objects.get(username='deleted')


class DopClass(models.Model):
    grat = models.ForeignKey(Class, on_delete=models.CASCADE)
    fra = models.ForeignKey(Class, null=True, on_delete=models.SET_NULL, related_name='fra_set')
    trt = models.ForeignKey(Class, default='UGbjbj', on_delete=models.SET_DEFAULT, related_name='trt_set')
    trirtj = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='trirtj_set')
    uyihok = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name='uyihok_set')
    ogohhbk = models.ForeignKey(Class, on_delete=models.SET(get_deleted_user_instance), related_name='ogohhbk_set')


class Garden(models.Model):
    name = models.CharField(max_length=77)


class OneTo(models.Model):
    name = models.OneToOneField(Garden, on_delete=models.CASCADE)
    name_link = models.CharField(max_length=70)


class Humans(models.Model):
    name = models.CharField(max_length=90, blank=True)
    apling = models.ManyToManyField(Garden)


class BabyChild(models.Model):
    name = models.CharField(max_length=77)






class ManyMotheland(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        BabyChild,
        through='BetweenModels',
        through_fields=('manymotheland', 'babychild', ),
    )


class BetweenModels(models.Model):
    manymotheland = models.ForeignKey(ManyMotheland, on_delete=models.CASCADE)
    babychild = models.ForeignKey(BabyChild, on_delete=models.CASCADE)
    invit = models.ForeignKey(
        BabyChild,
        on_delete=models.CASCADE,
        related_name="membership_invit",
    )



class FinishModel(models.Model):
    root = models.CharField(max_length=50)
    description = _("This text")


class HanFild(models.Field):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'char(25)'


class Mass(models.Model):
    description = HanFild()
    zail = models.CharField(max_length=46, null=True)


class Team(models.Model):
    SERMON = 'SR'
    JUNIOR = 'JN'
    YPPOR = 'YP '
    YEAR_IN_SCHOOL_CHOICES = [
        (SERMON, 'Sermon'),
        (JUNIOR, 'Junior'),
        (YPPOR, 'Yppor'),

    ]
    choises_fiels = models.CharField(
        max_length=12,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=JUNIOR,
    )


class Leam(models.Model):
    YEAR_IN_CHOICES = [
        ('TG', 'Tiger'),
        ('JN', 'Junior'),
        ('AS', 'Asistant')
    ]
    choises_fiels = models.CharField(max_length=2, choices=YEAR_IN_CHOICES, default='Tiger')
    name = models.CharField(max_length=33)





class Beam(models.Model):
    class BeamChoices(models.TextChoices):
        TIGER = 'TG', _('Tager')
        JUNIOR = 'JN', _('Junaar')
        ASISTANT = 'AS', _('Asistant')

    choises_fiels = models.CharField(max_length=133, choices=BeamChoices.choices, default='Tager')



class Meat(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),

    ]

    bone_choices = models.CharField(max_length=2,
                                    choices=YEAR_IN_SCHOOL_CHOICES,

                                    default='Freshman',
                                    )




class NAzz(models.Model):
    text = models.CharField(max_length=98)
    dop_text = models.TextField()




class Uniq(models.Model):
    cherif = models.CharField(max_length=45)
    help_text = "This my text"


def my_validator(value):
    if value[0] == 'J':
        raise ValidationError(
            _('Text do not begin with %(value)s'),
            params={'value': value},
        )


class Rkt(models.Model):
    tiyjkh = models.IntegerField(validators=[my_validator])


class AbstractClass(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Moon(AbstractClass):
    lug = models.CharField(max_length=5)





class Soon(models.Model):
    mbn = models.CharField(max_length=55)

    class Meta:
        ordering = ['mbn']


class Proverka_Uniq_Together(models.Model):
    deliver = models.CharField(max_length=77)
    cafe = models.CharField(max_length=77)

    class Meta:
        unique_together = [['deliver', 'cafe']]



class Pers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Pers):
    class Meta:
        proxy = True


class Omg(models.Model):
    fox = models.CharField(max_length=110)

    class Meta:
        verbose_name = 'Лиса'
        verbose_name_plural = 'Лисицы'


class Greet(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    fees = models.DateField(blank=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('additional_text', kwargs={'pk': self.pk})


class Yutug(models.Model):
    dop_text = models.CharField(max_length=88)
    first_name = models.CharField(max_length=97)
    slug = models.SlugField()

    @admin.display(ordering='first_name')
    def colored_first_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.dop_text,
            self.first_name,
        )


class Person(models.Model):
    first_name = models.CharField(max_length=50)



class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)















