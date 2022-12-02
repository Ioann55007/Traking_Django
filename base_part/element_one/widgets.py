from django.forms.widgets import Widget


class RichTextEditorWidget(Widget):
    template_name = 'django/forms/widgets/textarea.html'

    def __init__(self, attrs=None):
        default_attrs = {'cols': '80', 'rows': '20'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)




