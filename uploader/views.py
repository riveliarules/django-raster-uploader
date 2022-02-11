from fileinput import filename
import os
import werkzeug
from werkzeug.utils import secure_filename
from geo.Geoserver import Geoserver
import glob
from decouple import config

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.template import Context
from django.contrib import messages

from django_raster_uploader.settings import MEDIA_ROOT

# from .forms import RasterForm
# from .models import Rasterfile


class Home(TemplateView):
    template_name = 'home.html'


geo = Geoserver(config('GS_HOST'), username=config('GS_USERNAME'),
                password=config('GS_PASSWORD'))

ALLOWED_EXTENSIONS = {'tif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def store_exists(store_name, workspace = None):
    coverages_list = []
    response = False
    coverages_stores = geo.get_coveragestores(workspace)

    if type(coverages_stores) == 'str':
        return response
    
    if coverages_stores['coverageStores']:
        coverages_list = coverages_stores['coverageStores']['coverageStore']
    if store_name in [coverage['name'] for coverage in coverages_list]:
        return True


# essa função pega os workspaces do geoserver via API e passa a lista para a view html
def form(request):
    context = {}
    if request.method == 'GET':
        workspaces = geo.get_workspaces()['workspaces']['workspace']
        ws = [workspace['name'] for workspace in  workspaces]
    context['workspaces'] = ws
    return render(request, 'upload.html', context)


# função que sobe o arquivo inserido na view para a pasta 'media'
# obs: adicionar mensagens de erro ("flash")
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        if uploaded_file.name == '':
            messages.add_message(request, messages.WARNING, 'Nenhum arquivo selecionado!')
            return redirect("/")
        if uploaded_file and not allowed_file(uploaded_file.name):
            messages.add_message(request, messages.WARNING, 'Arquivo inválido!')
            return redirect("/")

        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)


        workspace_name = request.POST['workspace']
        file_name = MEDIA_ROOT + '/' + uploaded_file.name
        path = file_name
        store_name = (uploaded_file.name)[:-4]

        if uploaded_file:
            resultado = geo.create_coveragestore(
                path=path,
                workspace=workspace_name,
                layer_name=store_name,
                file_type="GeoTIFF",
                content_type="image/tiff"
            )
            print(path)
            os.remove(path)
            messages.add_message(request, messages.SUCCESS, 'Upload realizado com sucesso')
            return render(request, 'upload.html', context=None)
            
    return render(request, "/", context=None)
