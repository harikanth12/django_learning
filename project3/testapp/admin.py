from django.contrib import admin

from testapp.models import employee
# Register your models here.

class EmployeeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename']
    # fields = ['eno'] ## Fields are used to customize fields in the django admin panel;;
    fieldsets = [
        (None,{'fields':['eno']}),
        ('Profile details',{'fields':['ename','efname','elname','eaddr']}),
        ('Education details',{'fields':['eclass','emarks']})
    ]  # fields set is used customize fields and we can display the form data according to the required categories
      # only filedset or fields are used at a time
    search_fields = ['eno']
    list_per_page =1
    list_editable = ['eno']
    # list_display_links = ['eno']  ## list_display or list _editable or one used at a time
    list_filter = ['ename']
    # list_select_related = ['eno']
    ## startswith,endswith,istartswith,iendswith,range,in,filter,get,contains,exact,gt,igte,lt,ilte,icontains,iexact,


admin.site.register(employee,EmployeeeAdmin)

