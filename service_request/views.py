from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm, TrackRequestForm
from django.http import Http404, HttpResponse 

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
    return render(request, 'service_requests/track.html', {'service_request': service_request})


def track_requests(request):
    form = TrackRequestForm()

    if request.method == 'POST':
        form = TrackRequestForm(request.POST)
        if form.is_valid():
            customer_email = form.cleaned_data['customer_email']
            created_at = form.cleaned_data['created_at']
            
            try:
                service_request = ServiceRequest.objects.get(customer_email=customer_email, created_at__date=created_at)
                return render(request, 'service_requests/request_details.html', {'service_request': service_request})
            except ServiceRequest.DoesNotExist:
                return HttpResponse('No service request found for the provided details.', status=404)
    
    return render(request, 'service_requests/track_request.html', {'form': form})
