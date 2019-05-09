from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('station_name','Organization1_KindOfOG','organization1','organization2','organization3','organization4','organization5','organization6','line1','line2','line3','line4','line5','line6','line7','line8','line9','prefectures','city','memo')
        widgets = {
                    'station_name': forms.TextInput(attrs={'placeholder':'※「駅」は不要'}),
                    'furigana': forms.TextInput(attrs={'placeholder':'ひらがな'}),
                    'Organization1_KindOfOG': forms.RadioSelect(),
                    'organization1': forms.RadioSelect(),
                    'organization2': forms.RadioSelect(),
                    'organization3': forms.RadioSelect(),
                    'organization4': forms.RadioSelect(),
                    'organization5': forms.RadioSelect(),
                    'organization6': forms.RadioSelect(),
                    'line1': forms.TextInput(attrs={'placeholder':'JRが優先'}),
                    'line2': forms.TextInput(attrs={'placeholder':'2'}),
                    'line3': forms.TextInput(attrs={'placeholder':'3'}),
                    'line4': forms.TextInput(attrs={'placeholder':'4'}),
                    'line5': forms.TextInput(attrs={'placeholder':'5'}),
                    'line6': forms.TextInput(attrs={'placeholder':'6'}),
                    'line7': forms.TextInput(attrs={'placeholder':'7'}),
                    'line8': forms.TextInput(attrs={'placeholder':'8'}),
                    'line9': forms.TextInput(attrs={'placeholder':'9'}),
                    'prefectures': forms.TextInput(attrs={'placeholder':'例：神奈川県'}),
                    'city': forms.TextInput(attrs={'placeholder':'例：横浜市'}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
