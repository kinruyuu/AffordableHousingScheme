from django.db import models

class AhsPropertyLottery2(models.Model):
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    development = models.CharField(db_column='Development', max_length=255, blank=True, null=True)
    bed = models.IntegerField(db_column='Bed', blank=True, null=True)
    start_date = models.DateTimeField(db_column='Start_Date', blank=True, null=True)
    end_date = models.DateTimeField(db_column='End_Date', blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)
    omv = models.CharField(db_column='OMV', max_length=255, blank=True, null=True)
    sale_price = models.CharField(db_column='Sale_Price', max_length=255, blank=True, null=True)
    propertyid = models.CharField(db_column='PropertyID', max_length=255, blank=True, primary_key=True, null=False)
    phase = models.CharField(db_column='Phase', max_length=255, blank=True, null=True)
    lotterycase = models.CharField(db_column='LotteryCase', max_length=255, blank=True, null=True)
    lotterydate = models.CharField(db_column='LotteryDate', max_length=255, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)
    equity = models.CharField(db_column='Equity', max_length=255, blank=True, null=True)
    name_date = models.CharField(db_column='Name_Date', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahs_property_lottery_2'


class ChAhsSubmissionsLottery2(models.Model):
    applicationid = models.CharField(db_column='ApplicationID', max_length=18, primary_key=True, null=False)
    propertyid = models.CharField(db_column='PropertyID', max_length=14, blank=True, null=True)
    applicantname = models.CharField(db_column='ApplicantName', max_length=40, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=41, blank=True, null=True)
    development = models.CharField(db_column='Development', max_length=61, blank=True, null=True)
    stage = models.CharField(db_column='Stage', max_length=18, blank=True, null=True)
    saveurl = models.CharField(db_column='SaveURL', max_length=1, blank=True, null=True)
    applicationurl = models.CharField(db_column='ApplicationURL', max_length=1, blank=True, null=True)
    responseurl = models.CharField(db_column='ResponseURL', max_length=1, blank=True, null=True)
    ucrn = models.FloatField(db_column='UCRN', blank=True, null=True)
    propertyname = models.CharField(db_column='PropertyName', max_length=105, blank=True, null=True)
    submitdate = models.CharField(db_column='SubmitDate', max_length=11, blank=True, null=True)
    adults = models.BigIntegerField(db_column='Adults', blank=True, null=True)
    kids = models.BigIntegerField(db_column='Kids', blank=True, null=True)
    joint = models.CharField(db_column='Joint', max_length=4, blank=True, null=True)
    nationality = models.CharField(db_column='Nationality', max_length=6, blank=True, null=True)
    relationship = models.CharField(db_column='Relationship', max_length=11, blank=True, null=True)
    household_size = models.BigIntegerField(db_column='Household_Size', blank=True, null=True)
    jointname = models.CharField(db_column='JointName', max_length=8, blank=True, null=True)
    mortgageprovider = models.CharField(db_column='MortgageProvider', max_length=26, blank=True, null=True)
    resident = models.CharField(db_column='Resident', max_length=4, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=22, blank=True, null=True)
    residentvalid = models.CharField(db_column='ResidentValid', max_length=1, blank=True, null=True)
    incomevalid = models.CharField(db_column='IncomeValid', max_length=1, blank=True, null=True)
    depositvalid = models.CharField(db_column='DepositValid', max_length=1, blank=True, null=True)
    equityvalid = models.CharField(db_column='EquityValid', max_length=1, blank=True, null=True)
    mortgageamount = models.CharField(db_column='MortgageAmount', max_length=1, blank=True, null=True)
    helpbuyamount = models.CharField(db_column='HelpBuyAmount', max_length=1, blank=True, null=True)
    equity = models.CharField(db_column='Equity', max_length=1, blank=True, null=True)
    deposit = models.CharField(db_column='Deposit', max_length=1, blank=True, null=True)
    incomeoverall = models.CharField(db_column='IncomeOverall', max_length=1, blank=True, null=True)
    jointincomeoverall = models.CharField(db_column='JointIncomeOverall', max_length=1, blank=True, null=True)
    housesizevalid = models.CharField(db_column='HouseSizeValid', max_length=1, blank=True, null=True)
    taskurl = models.CharField(db_column='TaskURL', max_length=1, blank=True, null=True)
    parentid = models.CharField(db_column='ParentID', max_length=14, blank=True, null=True)
    age = models.CharField(db_column='Age', max_length=1, blank=True, null=True)
    jointage = models.CharField(db_column='JointAge', max_length=1, blank=True, null=True)
    county = models.CharField(db_column='County', max_length=1, blank=True, null=True)
    indublin = models.CharField(db_column='InDublin', max_length=1, blank=True, null=True)
    mortvalid = models.CharField(db_column='MortValid', max_length=1, blank=True, null=True)
    lotteryposition = models.CharField(db_column='LotteryPosition', max_length=1, blank=True, null=True)
    jointnationality = models.CharField(db_column='JointNationality', max_length=1, blank=True, null=True)
    jointrelationship = models.CharField(db_column='JointRelationship', max_length=1, blank=True, null=True)
    jointemail = models.CharField(db_column='JointEmail', max_length=1, blank=True, null=True)
    appealdate = models.CharField(db_column='AppealDate', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_ahs_submissions_lottery2'


class Allocation(models.Model):
    property = models.ForeignKey(AhsPropertyLottery2, on_delete=models.CASCADE)
    applicant = models.ForeignKey(ChAhsSubmissionsLottery2, on_delete=models.CASCADE)
    allocation_date = models.DateTimeField(auto_now_add=True)
