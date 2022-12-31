from django.contrib import admin, messages

from django.contrib.contenttypes.admin import GenericTabularInline
from django.db import models
from django.db.models import User
from django.utils.translation import ngettext, gettext_lazy
from django import forms
from .models import Alog, Logo, Class, DopClass, OneTo, Garden, Humans, BabyChild, ManyMotheland, \
    FinishModel, Mass, Team, Meat, NAzz, Uniq, Rkt, Moon, Soon, Pers, Proverka_Uniq_Together, Omg, Yutug, \
    Leam, Greet, Blog, Person, BetweenModels, Beam, Autocomplete, LinkAutocomplete, Membership, Pebon, Group, Image, \
    Product, Taos, BlogTemplate, Author, Comment
from .widgets import RichTextEditorWidget


@admin.register(Alog)
class AlogAdmin(admin.ModelAdmin):
    list_display = ('fery', 'date', 'vdate', 'gdate', 'cdate')
    fieldsets = [
        ('Text information', {'fields': ['arry']}),
        ('User information', {'fields': ['user']}),

        ('Email information', {'fields': ['eemail']}),
        ('Else information', {'fields': ['feld_field', 'file']})
    ]

    list_display_links = ('fery',)
    list_filter = ['date']
    date_hierarchy = 'date'
    save_on_top = True


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ("id", "imy_name", "slug", "ip_new", "file_path", "url")
    list_display_links = ("id", "imy_name", "slug", "ip_new", "file_path", "url")
    prepopulated_fields = {'slug': ('imy_name',)}
    list_filter = ['imy_name']


@admin.register(DopClass)
class DopClassAdmin(admin.ModelAdmin):
    list_display = ('grat', 'fra', 'trt', 'trirtj', 'uyihok', 'ogohhbk')


class DopClassInline(admin.TabularInline):
    model = DopClass
    fk_name = "grat"



@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    inlines = [DopClassInline]








@admin.register(OneTo)
class OneToAdmin(admin.ModelAdmin):
    list_display = ("name", "name_link")



@admin.register(Garden)
class GardenAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name']
    search_help_text = 'Search to eazy'


@admin.register(Humans)
class HumansAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ('apling',)


@admin.register(BabyChild)
class BabyChildAdmin(admin.ModelAdmin):
    list_display = ('name',)




@admin.register(ManyMotheland)
class ManyMothelandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FinishModel)
class FinishModelAdmin(admin.ModelAdmin):
    list_display = ('root', 'file_path', 'description')
    readonly_fields = ('file_path',)


@admin.register(Mass)
class MassAdmin(admin.ModelAdmin):
    list_display = ('description', 'zail')

@admin.register(Taos)
class TaosAdmin(admin.ModelAdmin):
    list_display = ('name', 'view_greet', 'agit')

    @admin.display(empty_value='Пропущенно это поле.')
    def view_greet(self, obj):
        return obj.greet


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('choises_fiels',)
    list_display_links = ('choises_fiels',)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username != 'Admin':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(Leam)
class LeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'choises_fiels')
    list_display_links = ('name', 'choises_fiels')
    actions = ['set_choic', 'update_choices']

    @admin.action(description='Install  choices Junior')
    def set_choic(self, request, queryset):
        message_update=queryset.update(choises_fiels='JN')
        self.message_user(request, ngettext(
            'You have succssesfully %d story',
            'You have succssesfully %d stories',
            message_update,
        ) % message_update, messages.SUCCESS)

    @admin.action(description='Install choices Asistant')
    def update_choices(self, request, queryset):
        queryset.update(choises_fiels='AS')


@admin.register(Meat)
class MeatAdmin(admin.ModelAdmin):
    list_display = ('bone_choices',)
    actions_on_bottom = True
    actions_on_top = False


@admin.register(NAzz)
class NAzzAdmin(admin.ModelAdmin):
    list_display = ('text',)
    formfield_overrides = {
        models.TextField: {'widget': RichTextEditorWidget},
    }


@admin.register(Uniq)
class UniqAdmin(admin.ModelAdmin):
    list_display = ('cherif', 'ty')
    save_as = True
    save_as_continue = False


@admin.register(Rkt)
class RktAdmin(admin.ModelAdmin):
    list_display = ('tiyjkh',)


@admin.register(Moon)
class MoonAdmin(admin.ModelAdmin):
    list_display = ('lug',)


@admin.register(Soon)
class SoonAdmin(admin.ModelAdmin):
    list_display = ('mbn',)


@admin.register(Pers)
class PersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Proverka_Uniq_Together)
class Proverka_Uniq_TogetherAdmin(admin.ModelAdmin):
    list_display = ('deliver', 'cafe')


class OmgAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("fox")

        if name[1] == 'd':
            msg = "You must write without this"
            self.add_error('fox', msg)


@admin.register(Omg)
class OmgAdmin(admin.ModelAdmin):
    list_display = ('fox',)
    form = OmgAdminForm



@admin.register(Greet)
class GreetAdmin(admin.ModelAdmin):
    exclude = ('fees',)
    view_on_site = False


@admin.register(Yutug)
class YutugAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'slug', 'colored_first_name')
    list_per_page = 2


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(first_name=request.user)

class MyInline(admin.TabularInline):
    model = Blog



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'author_first_name')
    list_display_links = ('author_first_name',)
    list_editable = ('title', 'author')
    list_select_related = ['author']

    @admin.display(ordering='author__first_name')
    def author_first_name(self, obj):
        return obj.author.first_name



@admin.register(BetweenModels)
class BetweenModelsAdmin(admin.ModelAdmin):
    list_display = ('manymotheland', 'babychild', 'invit')


@admin.register(Beam)
class BeamModelsAdmin(admin.ModelAdmin):
    radio_fields = {'choises_fiels': admin.VERTICAL}


@admin.register(Autocomplete)
class AutocompleteAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_name', 'date')
    ordering = ['date']
    search_fields = ['name']


@admin.register(LinkAutocomplete)
class LinkAutocompleteAdmin(admin.ModelAdmin):
    list_display = ('naf', 'link', 'flink', 'last_link', 'date')
    autocomplete_fields = ['flink']
    raw_id_fields = ('last_link',)



class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 4

@admin.register(Pebon)
class PebonAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


class ImageInline(GenericTabularInline):
    model = Image
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

@admin.register(BlogTemplate)
class BlogTemplateAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'title', 'blog_context', 'comment', 'slug', 'date')



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('salutation', 'name', 'email', 'headshot', 'last_accessed', 'created_by')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_comment', 'email', 'phone')
    list_display_links = ('author_comment',)



