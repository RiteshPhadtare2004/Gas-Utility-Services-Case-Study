from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('repair', 'Repair'),
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
    ]
    
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.customer_name} - {self.service_type}'
