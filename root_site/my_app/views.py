from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from gtts import gTTS
from pytils.translit import slugify

from .forms import InputForm
from .models import Storage


def index(request):
    return render(request, 'my_app/index.html')


def make_sound(title, text, lang):
    obj = gTTS(text=text, lang=lang, slow=False)
    obj_path = slugify(title)

    obj.save(f'media/audio/{obj_path}.mp3')
    return obj_path


def add(request):
    form = InputForm()

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            lang = form.cleaned_data['lang']
            lang_to_send = lang.code
            title_small = title.lower()
            try:
                Storage.objects.get(Q(title_small=title_small)
                                    | Q(slug=slugify(title)))
                return render(request, 'my_app/adding.html', {
                    'form': form,
                    'error': 'Така назва вже існує',
                })
            except:

                obj_path = make_sound(title, text, lang_to_send)
                Storage.objects.create(
                    title=form.cleaned_data['title'],
                    text=text,
                    lang=lang,
                    audio=f'/media/audio/{obj_path}.mp3',
                )
                return redirect(reverse('list'))

    return render(request, 'my_app/adding.html', {
        'form': form,
    })


class SoundList(ListView):
    model = Storage
    template_name = 'my_app/sound_list.html'
    context_object_name = 'sounds'
    ordering = ['-created_at']


class SoundDetail(DetailView):
    model = Storage
    template_name = 'my_app/sound_detail.html'
