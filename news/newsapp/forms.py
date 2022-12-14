from unicodedata import category
from django import forms
from newsapp import models
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

class UpdateProfile(UserChangeForm):
    username = forms.CharField(max_length=250,help_text="The Username field is required.")
    email = forms.EmailField(max_length=250,help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username','first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Password is Incorrect")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")

class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Stare hasło")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Nowe hasło")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Potwierdź nowe hasło")
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')

class savePost(forms.ModelForm):
    user = forms.CharField(max_length=30,label="Autor")
    category = forms.CharField(max_length=30,label="Kategoria")
    title = forms.CharField(max_length=250,label="Tytuł")
    short_description = forms.Textarea()
    content = forms.Textarea()
    meta_keywords = forms.Textarea()
    banner_path = forms.ImageField(label="Baner")
    status = forms.CharField(max_length=2)


    class Meta():
        model = models.Post
        fields = ('user', 'category', 'title', 'short_description', 'content', 'meta_keywords', 'banner_path', 'status',)

    def clean_category(self):
        catID = self.cleaned_data['category']
        try:
            category = models.Category.objects.get(id = catID)
            return category
        except:
            raise forms.ValidationError('Wybrana kategoria jest niewłaściwa')

    
    def clean_user(self):
        userID = self.cleaned_data['user']
        try:
            user = models.User.objects.get(id = userID)
            return user
        except:
            raise forms.ValidationError('Wybrany użytkownik jest niewłaściwy')


class saveComment(forms.ModelForm):
    post = forms.CharField(max_length=30,label="Post")
    name = forms.CharField(max_length=250,label="Name")
    email = forms.CharField(max_length=250,label="Email")
    subject = forms.CharField(max_length=250,label="Subject")
    message = forms.Textarea()
    class Meta():
        model = models.Comment
        fields = ('post', 'name', 'email', 'subject', 'message',)

    def clean_post(self):
        postID = self.cleaned_data['post']
        try:
            post = models.Post.objects.get(id = postID)
            return post
        except:
            raise forms.ValidationError('ID postu jest niewłaściwy')

    
