from django.shortcuts import render

# Create your views here.
def prodi1(request):
    judul = "Fakultas Pertanian"

    konteks = {
        'title': judul
    }
    return render(request, 'indexfaperta.html', konteks)
