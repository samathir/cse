from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import models
from .forms import Form


wordlist = models.WordPost.objects.order_by('-word_id')
if len(wordlist) == 0:
    id_num = 0
else:
    id_num = wordlist[0].word_id + 1

# initial request handle
def blank(request):
    folder = models.Image.objects.all()
    wordfolder = models.WordPost.objects.order_by('-word_id')
    # models.WordPost.objects.all().delete()
    filefolder = models.Files.objects.all()
    return render(request, 'static/html/index.html', {
        'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
    })
    return render(request, 'static/html/index.html')


def register(request):
    filefolder = models.Files.objects.all()
    folder = models.Image.objects.all()
    wfolder = models.WordPost.objects.order_by('-word_id')
    # wfolder = models.WordPost.objects.all()
    return render(request, 'static/html/show.html', {
        'folder': folder, 'wfolder': wfolder, 'filefolder': filefolder
    })
    # return render(request,'html/Register.html')


def friend(request):
    return render(request, 'static/html/DM_page.html')


def login(request):
    return render(request, 'static/html/Login.html')


## function handle upload.
def upload(request):
    if request.method == 'POST':
        uploaded = request.FILES['upload']
        fs = FileSystemStorage()
        filename = fs.save(uploaded.name, uploaded)
        uploaded_file_url = fs.url(filename)
        models.Image.objects.create(name=uploaded_file_url, like=0, comments='')
        folder = models.Image.objects.all()
        filefolder = models.Files.objects.all()
        wordfolder = models.WordPost.objects.order_by('-word_id')
        return render(request, 'static/html/index.html', {
            'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
        })
    return render(request, 'static/html/index.html')


def comment(request):
    if request.method == 'POST':
        data = request.POST
        pa = list(data)[1]
        income = data.__getitem__(pa)
        old = models.Image.objects.get(name=pa).comments
        updates = ""
        updates += old
        updates += income
        updates += '\n'
        models.Image.objects.filter(name=pa).update(comments=updates)
        print(models.Image.objects.get(name=pa).comments)
        # models.Image.objects.filter(name=pa).update(comments='')
    folder = models.Image.objects.all()
    filefolder = models.Files.objects.all()
    wordfolder = models.WordPost.objects.order_by('-word_id')
    return render(request, 'static/html/index.html', {
        'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
    })


def message(request):
    global id_num
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            models.WordPost.objects.create(word_id=id_num, message=message, like=0, comments='')
            id_num = id_num + 1
            folder = models.Image.objects.all()
            filefolder = models.Files.objects.all()
            wordfolder = models.WordPost.objects.order_by('-word_id')
            return render(request, 'static/html/index.html', {
                'wordfolder': wordfolder,
                'folder': folder,
                'filefolder': filefolder})


def like(request):
    if request.method == 'POST':
        data = request.POST
        pa = list(data)[1]
        value = models.Image.objects.get(name=pa).like
        models.Image.objects.filter(name=pa).update(like=value + 1)
        folder = models.Image.objects.all()
        filefolder = models.Files.objects.all()
        wordfolder = models.WordPost.objects.order_by('-word_id')
        return render(request, 'static/html/index.html', {
            'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
        })
    return render(request, 'static/html/index.html')


def textlikes(request):
    if request.method == 'POST':
        data = request.POST
        pa = list(data)[1]
        value = models.WordPost.objects.get(word_id=pa).like
        models.WordPost.objects.filter(word_id=pa).update(like=value + 1)
        folder = models.Image.objects.all()
        filefolder = models.Files.objects.all()
        wordfolder = models.WordPost.objects.order_by('-word_id')
        return render(request, 'static/html/index.html', {
            'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
        })
        # if form.is_valid():
        # me = form.cleaned_data['datetime']
        # print(me)
        # value=models.WordPost.objects.get(message=me).like
        # models.WordPost.objects.filter(datetime=me).update(like=models.WordPost.objects.get(datetime=me).like+1)
        # folder = models.Image.objects.all()
        # wordfolder = models.WordPost.objects.order_by('-datetime')
        # return render(request, 'html/index.html', {
        # 'folder': folder, 'wordfolder': wordfolder
        # })
    return render(request, 'static/html/index.html')


def textcomment(request):
    if request.method == 'POST':
        data = request.POST
        pa = list(data)[1]
        print(pa)
        income = data.__getitem__(pa)
        old = models.WordPost.objects.get(message=pa).comments
        updates = ""
        updates += old
        updates += income
        updates += '\n'
        models.WordPost.objects.filter(message=pa).update(comments=updates)
        print(models.WordPost.objects.get(message=pa).comments)
        # models.Image.objects.filter(name=pa).update(comments='')
        folder = models.Image.objects.all()
        filefolder = models.Files.objects.all()
        wordfolder = models.WordPost.objects.order_by('-word_id')
        return render(request, 'static/html/index.html', {
            'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
        })
    return render(request, 'static/html/index.html')


def files(request):
    if request.method == 'POST':
        uploaded = request.FILES['uploaded']
        fs = FileSystemStorage()
        filename = fs.save(uploaded.name, uploaded)
        uploaded_file_url = fs.url(filename)
        models.Files.objects.create(name=uploaded_file_url, like=0, comments='')
        folder = models.Image.objects.all()
        wordfolder = models.WordPost.objects.order_by('-word_id')
        filefolder = models.Files.objects.all()
        return render(request, 'static/html/index.html', {
            'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
        })
    return render(request, 'static/html/index.html')


def filec(request):
    if request.method == 'POST':
        data = request.POST
        pa = list(data)[1]
        income = data.__getitem__(pa)
        old = models.Files.objects.get(name=pa).comments
        updates = ""
        updates += old
        updates += income
        updates += '\n'
        models.Files.objects.filter(name=pa).update(comments=updates)
        print(models.Files.objects.get(name=pa).comments)
        # models.Image.objects.filter(name=pa).update(comments='')
        filefolder = models.Files.objects.all()
        folder = models.Image.objects.all()
        wordfolder = models.WordPost.objects.order_by('-word_id')
    return render(request, 'static/html/index.html', {
        'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
    })


def filel(request):
    if request.method == 'POST':
        data = request.POST
        pa = list(data)[1]
        value = models.Files.objects.get(name=pa).like
        models.Files.objects.filter(name=pa).update(like=value + 1)
        filefolder = models.Files.objects.all()
        folder = models.Image.objects.all()
        wordfolder = models.WordPost.objects.order_by('-word_id')
        return render(request, 'static/html/index.html', {
          'folder': folder, 'wordfolder': wordfolder, 'filefolder': filefolder
        })
    return render(request, 'static/html/index.html')


# websocket
def chat(request):
    return render(request, 'chat/templates/chat/base.html')
