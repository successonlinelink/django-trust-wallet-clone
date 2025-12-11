from django.contrib import admin
from .models import Phrase, PrivateKey, KeyStore, Wallets, Qrcodes, SendCoin, News, Comment
# Balance

class WalletsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    prepopulated_fields = {'pid': ('title', )}

class PhraseAdmin(admin.ModelAdmin):
    list_display = ['user', 'phrase', 'content', 'date', 'wallet_name']
    prepopulated_fields = {'pid': ('phrase', )}

class PrivateKeyFormAdmin(admin.ModelAdmin):
    list_display = ['private_key', 'user', 'date', 'wallet_name']
    prepopulated_fields = {'pid': ('private_key', )}

class KeyStoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'key_store', 'content', 'date', 'wallet_name']
    prepopulated_fields = {'kid': ('key_store', )}

class QrcodesAdmin(admin.ModelAdmin):
    list_display = ['wallet_name', 'qrcode', 'tid']
    prepopulated_fields = {'tid': ('wallet_name', )}

class SendCoinAdmin(admin.ModelAdmin):
    list_display = ['w_address', 'amount', 'sid']
    prepopulated_fields = {'sid': ('w_address', )}


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'nid': ('title', )}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']
    prepopulated_fields = {'cid': ('content', )}
    
    
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(PrivateKey, PrivateKeyFormAdmin)
admin.site.register(KeyStore, KeyStoreAdmin)
admin.site.register(Wallets, WalletsAdmin)
admin.site.register(Qrcodes, QrcodesAdmin)
admin.site.register(SendCoin, SendCoinAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)






