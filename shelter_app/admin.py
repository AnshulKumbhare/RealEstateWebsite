from django.contrib import admin
from shelter_app.models import testimonial, contact, shelteragents, shelterproperties

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'testimony', 'tpname', 'position', 'companyname']

admin.site.register(testimonial, TestimonialAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'middlename', 'lastname', 'email', 'mob1', 'mob2', 'address', 'msg']

admin.site.register(contact, ContactAdmin)

class ShelterAgentsAdmin(admin.ModelAdmin):
    list_display = ['id','agentname', 'year', 'psold', 'agentimage', 'is_active']
    list_filter = ['is_active']

admin.site.register(shelteragents, ShelterAgentsAdmin)

class ShelterPropertiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'middlename', 'lastname', 'email', 'mob1', 'mob2', 'address', 'city', 'propertyname', 'ptype1', 'ptype2', 'beds', 'area', 'price', 'description', 'pimage']
    list_filter = ['ptype1', 'ptype2', 'city']

admin.site.register(shelterproperties, ShelterPropertiesAdmin)