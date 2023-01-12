from django.forms import ModelForm

from .models import Board

class BoardForm(ModelForm):
    class Meta:
        model = Board       # модель в которую запись из формы
        fields = (          # поля которые присутствуют в форме 
            'title',
            "content",
            "price",
            "rubric"
        )
        # fields = ("__all__")  # все поля
