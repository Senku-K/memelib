from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse
from django.utils import timezone
from .models import Meme
from .forms import MemeForm

def meme_list(request):
    memes = Meme.objects.all().order_by('-upload_date')
    return render(request, 'memes/meme_list.html', {'memes': memes})

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def upload_meme(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.uploader = request.user
            meme.save()
            messages.success(request, 'Meme uploaded successfully!')
            return redirect('meme_list')
    else:
        form = MemeForm()
    return render(request, 'memes/upload_meme.html', {'form': form})

def download_meme(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    meme.increment_downloads()
    response = FileResponse(meme.image)
    response['Content-Disposition'] = f'attachment; filename="{meme.title}.jpg"'
    return response

@login_required
def like_meme(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    if request.user in meme.likes.all():
        meme.likes.remove(request.user)
    else:
        meme.likes.add(request.user)
    return redirect('meme_list') 
