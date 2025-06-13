from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Korxona
from .forms import KorxonaForm
from django.db.models import Q
from django.db.models import Count
import json


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
        sort = self.request.GET.get('sort', '')

        queryset = Korxona.objects.all()

        if qidiruv:
            queryset = queryset.filter(
                Q(nomi__icontains=qidiruv) | Q(faoliyat_turi__icontains=qidiruv)
            )

        if sort == 'nomi':
            queryset = queryset.order_by('nomi')
        elif sort == 'sanasi':
            queryset = queryset.order_by('ochilgan_sana')  # modelda bu maydon bo‘lishi kerak
        elif sort == 'ishchilar':
            queryset = queryset.order_by('-ishchilar_soni')  # modelda bu maydon bo‘lishi kerak
        elif sort == 'yangi':
            queryset = queryset.order_by('-id')  # eng so‘nggi qo‘shilganlar

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qidiruv'] = self.request.GET.get('q', '')
        context['sort'] = self.request.GET.get('sort', '')
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


class KorxonaStatistikaView(TemplateView):
    template_name = 'korxona_statistika.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stat = (
            Korxona.objects.values('faoliyat_turi')
            .annotate(sanoq=Count('id'))
            .order_by('-sanoq')
        )

        # Diagramma uchun
        context['labels'] = json.dumps([item['faoliyat_turi'] for item in stat])
        context['values'] = json.dumps([item['sanoq'] for item in stat])

        # Jadval uchun
        context['stat_data'] = stat
        return context


# Aloqa sahifasi
class ContactView(TemplateView):
    template_name = 'contact.html'
