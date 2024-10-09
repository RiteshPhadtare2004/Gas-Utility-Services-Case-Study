from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.http import Http404

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('track_request', pk=form.instance.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def track_request(request, pk):
    try:
        service_request = ServiceRequest.objects.get(pk=pk)
    except ServiceRequest.DoesNotExist:
        raise Http404("Request does not exist.")
    return render(request, 'service_requests/track_request.html', {'service_request': service_request})
