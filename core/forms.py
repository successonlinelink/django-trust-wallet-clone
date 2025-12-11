from django import forms
from django.forms import ModelForm
from django.forms import ImageField, FileInput, TextInput, Select

from .models import Phrase, KeyStore, PrivateKey, SendCoin, Comment

# Phrase
class PhraseForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': '', 'placeholder':'Wallet Phrase'}), required=True)
    phrase = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Wallet Username/Email'}), required=True)
    wallet_name = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Wallet Name'}), required=True)


    class Meta:
        model = Phrase
        fields = ['phrase', 'content', 'wallet_name']
    
    # this guy will apply automatic class to all the fields with class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control" 

# KeyStore
class KeyStoreForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': '', 'placeholder':'Keystone Json'}), required=True)
    key_store = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Wallet Password'}), required=True)
    wallet_name = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Wallet Name'}), required=True)

    class Meta:
        model = KeyStore
        fields = ['key_store', 'content', 'wallet_name']
    
    # this guy will apply automatic class to all the fields with class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control" 

# PrivateKey
class PrivateKeyForm(ModelForm):
    private_key = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Enter Your Private Key'}), required=True)
    wallet_name = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Wallet Name'}), required=True)

    class Meta:
        model = PrivateKey
        fields = ['private_key', 'wallet_name']
    
    # this guy will apply automatic class to all the fields with class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control" 

# Phrase
class SendCoinForm(ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'class': '', 'placeholder':'Wallet Phrase'}), required=True)
    w_address = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Receiver Wallet Address'}), required=True)
    amount = forms.CharField(widget=forms.TextInput(attrs={'class': '', "placeholder":"0.00"}), required=True)
    note = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Please enter Remark'}), required=True)

    class Meta:
        model = SendCoin
        fields = ['w_address', 'note', 'amount']
    
    # this guy will apply automatic class to all the fields with class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "clear-ip value_input ip-style2" 

# Comment
class CommentForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': '', 'placeholder':'Comment Here...'}), required=True)

    class Meta:
        model = Comment
        fields = ['content']
    
    # this guy will apply automatic class to all the fields with class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "cmnt-input" 
