from django.forms import ModelForm
from .models import FileUpload

class FileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'
