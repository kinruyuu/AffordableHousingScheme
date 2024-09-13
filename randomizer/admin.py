from django.contrib import admin
from .models import AhsPropertyLottery2, ChAhsSubmissionsLottery2, Allocation

@admin.register(AhsPropertyLottery2)
class AhsPropertyLottery2Admin(admin.ModelAdmin):
    list_display = ('propertyid', 'name', 'development', 'status', 'lotterydate')
    search_fields = ('name', 'development', 'status')

@admin.register(ChAhsSubmissionsLottery2)
class ChAhsSubmissionsLottery2Admin(admin.ModelAdmin):
    list_display = ('applicationid', 'applicantname', 'email', 'lotteryposition')
    search_fields = ('applicantname', 'email')

@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    list_display = ('property', 'applicant', 'allocation_date')
    search_fields = ('property__name', 'applicant__applicantname')
