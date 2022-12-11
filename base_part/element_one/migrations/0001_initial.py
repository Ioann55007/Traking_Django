# Generated by Django 4.1.3 on 2022-12-10 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import element_one.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('tit', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Autocomplete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('text_name', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BabyChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=77)),
            ],
        ),
        migrations.CreateModel(
            name='Beam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choises_fiels', models.CharField(choices=[('TG', 'Tager'), ('JN', 'Junaar'), ('AS', 'Asistant')], default='Tager', max_length=133)),
            ],
        ),
        migrations.CreateModel(
            name='BetweenModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('babychild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element_one.babychild')),
                ('invit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_invit', to='element_one.babychild')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_class', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='FinishModel',
            fields=[
                ('root', models.CharField(max_length=50)),
                ('file_path', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=77)),
            ],
        ),
        migrations.CreateModel(
            name='Greet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.TextField(blank=True)),
                ('fees', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Leam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choises_fiels', models.CharField(choices=[('TG', 'Tiger'), ('JN', 'Junior'), ('AS', 'Asistant')], default='Tiger', max_length=2)),
                ('name', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.GenericIPAddressField(unpack_ipv4=True)),
                ('slug', models.SlugField()),
                ('imy_name', models.CharField(max_length=80)),
                ('ip_new', models.TextField()),
                ('file_path', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Mass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', element_one.models.HanFild()),
                ('zail', models.CharField(blank=True, max_length=46, null=True)),
                ('ibjbk', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bone_choices', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore')], default='Freshman', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('lug', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NAzz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=98)),
                ('dop_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Omg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fox', models.CharField(max_length=110)),
            ],
            options={
                'verbose_name': 'Лиса',
                'verbose_name_plural': 'Лисицы',
            },
        ),
        migrations.CreateModel(
            name='Pebon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Pers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiyjkh', models.IntegerField(validators=[element_one.models.my_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Soon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbn', models.CharField(max_length=55)),
            ],
            options={
                'ordering': ['mbn'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choises_fiels', models.CharField(choices=[('SR', 'Sermon'), ('JN', 'Junior'), ('YP ', 'Yppor')], default='JN', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Uniq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cherif', models.CharField(max_length=45)),
                ('ty', models.TextField(help_text='This my text')),
            ],
        ),
        migrations.CreateModel(
            name='Yutug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop_text', models.CharField(max_length=88)),
                ('first_name', models.CharField(max_length=97)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Proverka_Uniq_Together',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver', models.CharField(max_length=77)),
                ('cafe', models.CharField(max_length=77)),
            ],
            options={
                'unique_together': {('deliver', 'cafe')},
            },
        ),
        migrations.CreateModel(
            name='OneTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_link', models.CharField(max_length=70)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='element_one.garden')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element_one.group')),
                ('pebon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element_one.pebon')),
            ],
        ),
        migrations.CreateModel(
            name='ManyMotheland',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('members', models.ManyToManyField(through='element_one.BetweenModels', to='element_one.babychild')),
            ],
        ),
        migrations.CreateModel(
            name='LinkAutocomplete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naf', models.CharField(max_length=90)),
                ('date', models.DateField(auto_now_add=True)),
                ('flink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flink_set', to='element_one.autocomplete')),
                ('last_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_link_set', to='element_one.autocomplete')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_set', to='element_one.autocomplete')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Humans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=90)),
                ('apling', models.ManyToManyField(to='element_one.garden')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='element_one.Membership', to='element_one.pebon'),
        ),
        migrations.CreateModel(
            name='DopClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fra_set', to='element_one.class')),
                ('grat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element_one.class')),
                ('ogohhbk', models.ForeignKey(on_delete=models.SET(element_one.models.get_deleted_user_instance), related_name='ogohhbk_set', to='element_one.class')),
                ('trirtj', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='trirtj_set', to='element_one.class')),
                ('trt', models.ForeignKey(default='UGbjbj', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='trt_set', to='element_one.class')),
                ('uyihok', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='uyihok_set', to='element_one.class')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element_one.person')),
            ],
        ),
        migrations.AddField(
            model_name='betweenmodels',
            name='manymotheland',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element_one.manymotheland'),
        ),
        migrations.CreateModel(
            name='Alog',
            fields=[
                ('fery', models.AutoField(primary_key=True, serialize=False)),
                ('arry', models.CharField(max_length=110)),
                ('date', models.DateField(auto_now=True)),
                ('vdate', models.DateField(auto_now_add=True)),
                ('gdate', models.DateTimeField(auto_now=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('eemail', models.EmailField(max_length=254)),
                ('feld_field', models.DurationField()),
                ('file', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyPerson',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('element_one.pers',),
        ),
    ]
