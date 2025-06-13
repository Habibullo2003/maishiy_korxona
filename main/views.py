from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Korxona
from .forms import KorxonaForm
from django.db.models import Q


# Bosh sahifa
class HomeView(TemplateView):
    template_name = 'home.html'


# Korxonalar ro'yxati (qidiruvli)
class KorxonaListView(ListView):
    model = Korxona
    template_name = 'korxona_list.html'
    context_object_name = 'korxonalar'

    def get_queryset(self):
        qidiruv = self.request.GET.get('q', '')
        if qidiruv:
            return Korxona.objects.filter(
                Q(nomi__icontains=qidiruv) | Q(faoliyat_turi__icontains=qidiruv)
            )
        return Korxona.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qidiruv'] = self.request.GET.get('q', '')
        return context


# Yangi korxona qo‘shish
class KorxonaCreateView(CreateView):
    model = Korxona
    form_class = KorxonaForm
    template_name = 'korxona_add.html'
    success_url = reverse_lazy('korxona_list')


# Korxonani tahrirlash
class KorxonaUpdateView(UpdateView):
    model = Korxona
    form_class = KorxonaForm
    template_name = 'korxona_edit.html'
    success_url = reverse_lazy('korxona_list')


# Korxonani uchirish
class KorxonaDeleteView(DeleteView):
    model = Korxona
    template_name = 'korxona_confirm_delete.html'
    success_url = reverse_lazy('korxona_list')


# Aloqa sahifasi
class ContactView(TemplateView):
    template_name = 'contact.html'
