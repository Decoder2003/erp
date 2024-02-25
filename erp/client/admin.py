from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# ---- user ----
class userResource(resources.ModelResource):
    class Meta:
        model = User

@admin.register(User)
class userAdmin(ImportExportModelAdmin):
    resource_class = userResource
# -------------

# ---- institution ----
class institutionResource(resources.ModelResource):
    class Meta:
        model = institution
@admin.register(institution)
class institutionAdmin(ImportExportModelAdmin):
    resource_class = institutionResource
    list_display = ("id","name",)
    search_fields = ("id","name",)
# ---------------------
    
# ---- degree ----
class degreeResource(resources.ModelResource):
    class Meta:
        model = degree
@admin.register(degree)
class degreeAdmin(ImportExportModelAdmin):
    resource_class = degreeResource
    list_display = ("id","name",)
    search_fields = ("id","name",)
# ---------------------
    
# ---- fieldofstudy ----
class field_of_studyResource(resources.ModelResource):
    class Meta:
        model = field_of_study
@admin.register(field_of_study)
class field_of_studyAdmin(ImportExportModelAdmin):
    resource_class = field_of_studyResource
    list_display = ("id","name",)
    search_fields = ("id","name",)
# ---------------------
    
# ---- education ----
class educationResource(resources.ModelResource):
    class Meta:
        model = education
@admin.register(education)
class educationAdmin(ImportExportModelAdmin):
    resource_class = educationResource
    list_display = ("id","userId","institution","field_of_study","start_date","end_date")
    search_fields = ("id",)
# ---------------------

# ---- feed ----
class feedResource(resources.ModelResource):
    class Meta:
        model = feed
@admin.register(feed)
class feedAdmin(ImportExportModelAdmin):
    resource_class = feedResource
    list_display = ("id","userId","time_stamp",)
    search_fields = ("id",)
# ---------------------
    
# ---- image ----
class imageResource(resources.ModelResource):
    class Meta:
        model = image
@admin.register(image)
class imageAdmin(ImportExportModelAdmin):
    resource_class = imageResource
    list_display = ("id","feedId","image_url",)
    list_display_links = ("id","image_url",)
    search_fields = ("id",)
# ---------------------
    
# ---- interaction ----
class interactionResource(resources.ModelResource):
    class Meta:
        model = interaction
@admin.register(interaction)
class interactionAdmin(ImportExportModelAdmin):
    resource_class = interactionResource
    list_display = ("id","feedId","userId","interaction_type",)
    search_fields = ("id",)
# ---------------------
    
# ---- group ----
class groupResource(resources.ModelResource):
    class Meta:
        model = group
@admin.register(group)
class groupAdmin(ImportExportModelAdmin):
    resource_class = groupResource
    list_display = ("id","name","userId","is_active","image_url",)
    search_fields = ("id","image_url",)
# ---------------------
    
# ---- group ----
class group_membershipResource(resources.ModelResource):
    class Meta:
        model = group_membership
@admin.register(group_membership)
class group_membershipAdmin(ImportExportModelAdmin):
    resource_class = group_membershipResource
    list_display = ("id","groupId","userId","is_admin",)
    search_fields = ("id",)
# ---------------------
    
# ---- post ----
class postResource(resources.ModelResource):
    class Meta:
        model = post
@admin.register(post)
class postAdmin(ImportExportModelAdmin):
    resource_class = postResource
    list_display = ("id","groupId","userId","time_stamp",)
    search_fields = ("id",)
# ---------------------
    
# ---- event ----
class eventResource(resources.ModelResource):
    class Meta:
        model = event
@admin.register(event)
class eventAdmin(ImportExportModelAdmin):
    resource_class = eventResource
    list_display = ("id","groupId","title","time_stamp",)
    search_fields = ("id",)
# ---------------------