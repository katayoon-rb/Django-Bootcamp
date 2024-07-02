from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Trip, Note

class HomeView(TemplateView):
    template_name = 'trip/index.html'
    
    
# LIST
def trip_list(request):
    context = {
        'trips': Trip.objects.filter(owner=request.user)
    }
    return render(request, 'trip/trip_list.html', context)

class NoteListView(ListView):
    model = Note
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset

# CREATE 
class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"
    
    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form
    
class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
# TRIP
class TripDetailView(DetailView):
    model = Trip
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['object'].notes.all()
        return context
    
class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ["city", "country", "start_date", "end_date"]

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    
    
# NOTE
class NoteDetailView(DetailView):
    model = Note
    
class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"
    
    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form
    
class NoteDeleteview(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    