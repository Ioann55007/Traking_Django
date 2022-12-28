import uuid
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Alog(models.Model):
    objects = models.Manager()
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

    def __str__(self):
        return self.arry


class Logo(models.Model):
    id = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    slug = models.SlugField()
    imy_name = models.CharField(max_length=80)
    ip_new = models.TextField()
    file_path = models.UUIDField(primary_key=True, default=uuid.uuid4)
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

    def __str__(self):
        return self.name


class OneTo(models.Model):
    name = models.OneToOneField(Garden, on_delete=models.CASCADE)
    name_link = models.CharField(max_length=70)


class Humans(models.Model):
    name = models.CharField(max_length=90, blank=True)
    apling = models.ManyToManyField(Garden)


class BabyChild(models.Model):
    name = models.CharField(max_length=77)

    def __str__(self):
        return self.name


class ManyMotheland(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        BabyChild,
        through='BetweenModels',
        through_fields=('manymotheland', 'babychild', ),
    )

    def __str__(self):
        return self.name


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
    file_path = models.UUIDField(primary_key=True, default=uuid.uuid4)
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
    zail = models.CharField(max_length=46)



class Taos(models.Model):
    name = models.CharField(max_length=15)
    greet = models.CharField(max_length=10, blank=True, null=True)
    agit = models.TextField()




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

    def __str__(self):
        return self.choises_fiels



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
    ty = models.TextField(help_text="This my text")

    def __str__(self):
        return self.cherif


def my_validator(value):
    if value[0] == 'J':
        raise ValidationError(
            _('Text do not begin with %(value)s'),
            params={'value': value},
        )


class Rkt(models.Model):
    tiyjkh = models.CharField(max_length=110, validators=[my_validator])


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
    title = models.TextField(blank=True)
    fees = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse('element_one:additional_text', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


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
    objects = models.Manager()
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)


class Autocomplete(models.Model):
    name = models.CharField(max_length=90)
    text_name = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class LinkAutocomplete(models.Model):
    naf = models.CharField(max_length=90)
    link = models.ForeignKey(Autocomplete, on_delete=models.CASCADE, related_name='link_set')
    flink = models.ForeignKey(Autocomplete, on_delete=models.CASCADE, related_name='flink_set')
    last_link = models.ForeignKey(Autocomplete, on_delete=models.CASCADE, related_name='last_link_set')
    date = models.DateField(auto_now_add=True)



class Pebon(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Pebon, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    pebon = models.ForeignKey(Pebon, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Image(models.Model):
    image = models.ImageField(upload_to="")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Product(models.Model):
    name = models.CharField(max_length=100)



class BlogTemplate(models.Model):
    objects = models.Manager()
    date = models.DateField(auto_now=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    blog_context = models.TextField()
    comment = models.ForeignKey('Comment', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=130,  default=uuid.uuid1, blank=True)


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='')
    last_accessed = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})




class Comment(models.Model):
    name =  models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.IntegerField()
    messages = models.TextField()






