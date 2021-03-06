from django import forms
from .models import UserAnswer
from django.forms.widgets import RadioSelect
from .models import CorrectAnswer



class AnswerForm(forms.ModelForm):
    textAnswer = forms.ModelChoiceField(queryset=CorrectAnswer.objects.none(),
                                        widget=RadioSelect,
                                        required=False,
                                        label=" "
                                        )

    class Meta:
        model = UserAnswer
        fields = ('textAnswer',)


    def __init__(self,type,question,*args,**kwargs) :

        super(AnswerForm,self).__init__(*args,**kwargs)
        self.type = type
        if type == 'mcq':
            
            self.fields['textAnswer']  = forms.ChoiceField(choices=CorrectAnswer.objects.filter(questionID = question.questionID).values_list('correctAnswerID','answer'), widget= RadioSelect, required=False, label="")
            self.fields['textAnswer'].widget.attrs.update({
                'class':'btn bg-light'
            })
            
        else:
            self.fields['textAnswer'] = forms.CharField(max_length=50, required=False,)

    def clean(self) :
        if self.type!='mcq':
            textAnswer = self.cleaned_data['textAnswer']
            if textAnswer.strip().isalpha() is False:
                if len(textAnswer.strip())==0:
                    return super().clean()
                raise forms.ValidationError('No Numeric or symbols allowed in answer')
    
        

          

