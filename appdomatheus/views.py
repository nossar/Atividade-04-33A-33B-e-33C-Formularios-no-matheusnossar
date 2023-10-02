from django.shortcuts import render, redirect
from .models import MusicosFavoritos, BandasFavoritas

def home(request):
  musicos = MusicosFavoritos.objects.all()
  bandas = BandasFavoritas.objects.all()
  return render(request, "home.html", context={ "musicos_favoritos": musicos, "bandas_favoritas": bandas })

def insert_musico(request):
  if request.method == "POST":
    MusicosFavoritos.objects.create(
      nome = request.POST["nome"],
      data_de_nascimento = request.POST["data_de_nascimento"],
      banda = request.POST["banda"],
      instrumento = request.POST["instrumento"]
    )
    return redirect("home")
  return render(request, "forms.html", context={"tipo": "Adicionar"})

def insert_banda(request):
  if request.method == "POST":
    BandasFavoritas.objects.create(
      nome = request.POST["nome"],
      ano_de_inicio = request.POST["ano_de_inicio"],
      popularidade = request.POST["popularidade"],
      estilo = request.POST["estilo"]
    )
    return redirect("home")
  return render(request, "forms_banda.html", context={"tipo": "Adicionar"})

def update_musico(request, id):
  musico = MusicosFavoritos.objects.get(id = id)
  if request.method == "POST":
      musico.nome = request.POST["nome"]
      musico.data_de_nascimento = request.POST["data_de_nascimento"]
      musico.banda = request.POST["banda"]
      musico.instrumento = request.POST["instrumento"]
      musico.save()
    
      return redirect("home")
  return render(request, "forms.html", context={"tipo": "Atualizar", "artista": musico})

def update_banda(request, id):
  banda = BandasFavoritas.objects.get(id = id)
  if request.method == "POST":
      banda.nome = request.POST["nome"]
      banda.ano_de_inicio = request.POST["ano_de_inicio"]
      banda.popularidade = request.POST["popularidade"]
      banda.estilo = request.POST["estilo"]
      banda.save()
    
      return redirect("home")
  return render(request, "forms_banda.html", context={"tipo": "Atualizar", "banda": banda})

def delete_musico(request, id):
  musico = MusicosFavoritos.objects.get(id = id)
  if request.method == "POST":
      if "confirmar" in request.POST:
        musico.delete()
    
      return redirect("home")
  return render(request, "are_you_sure.html", context={"artista": musico})
  
def delete_banda(request, id):
  banda = BandasFavoritas.objects.get(id = id)
  if request.method == "POST":
      if "confirmar" in request.POST:
        banda.delete()
    
      return redirect("home")
  return render(request, "are_you_sure_banda.html", context={"banda": banda})