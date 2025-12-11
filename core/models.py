from django.db import models
from userauths.models import User

import shortuuid
from shortuuid.django_fields import ShortUUIDField



# wallets
class Wallets(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.user.username

    class Meta:
        ordering = ["-date"]


# Phrase
class Phrase(models.Model):
    pid = ShortUUIDField(length=15, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # phrase_wallet = models.ForeignKey(Wallets, on_delete=models.CASCADE)

    wallet_name = models.CharField(max_length=100, blank=True, null=True)
    phrase = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=2000, blank=True, null=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.phrase:
            return self.phrase
        else:
            return self.user.username

    class Meta:
        ordering = ["-date"]

# KeyStore
class KeyStore(models.Model):
    kid = ShortUUIDField(length=15, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=100, blank=True, null=True)
    key_store = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=2000, blank=True, null=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.key_store:
            return self.key_store
        else:
            return self.user.username

    class Meta:
        ordering = ["-date"]


# PrivateKey
class PrivateKey(models.Model):
    pid = ShortUUIDField(length=15, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=100, blank=True, null=True)
    private_key = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        if self.private_key:
            return self.private_key
        else:
            return self.user.username

    class Meta:
        ordering = ["-date"]


# qrc
class Qrcodes(models.Model):
    tid = ShortUUIDField(length=7, max_length=25, alphabet=shortuuid.get_alphabet())
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    token = models.CharField(max_length=100, blank=True, null=True)
    wallet_name = models.CharField(max_length=100, blank=True, null=True)
    qrcode = models.ImageField(upload_to='image', blank=True, null=True)
    logo = models.ImageField(upload_to='image', blank=True, null=True)

    
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.wallet_name


    class Meta:
        ordering = ["-date"]


# Send
class SendCoin(models.Model):
    sid = ShortUUIDField(length=7, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    w_address = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField(default=0.00)
    note = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.w_address

    class Meta:
        ordering = ["-date"]

# convert
class Convert(models.Model):
    
    convert = models.IntegerField(default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.convert

    class Meta:
        ordering = ["-date"]

# balance
class Balance(models.Model):
    bid = ShortUUIDField(length=7, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.bid

    class Meta:
        ordering = ["-date"]

# news
class News(models.Model):
    nid = ShortUUIDField(length=7, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=5000, blank=True, null=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    mins_read = models.CharField(max_length=100, blank=True, null=True)

    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]
        
        
# comment
class Comment(models.Model):
    cid = ShortUUIDField(length=7, max_length=25, alphabet=shortuuid.get_alphabet())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content = models.TextField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-date"]
        
  