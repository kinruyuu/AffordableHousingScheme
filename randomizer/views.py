from django.shortcuts import render, redirect
from .models import AhsPropertyLottery2, ChAhsSubmissionsLottery2
import random, csv
from datetime import datetime
from django.core.mail import EmailMessage
from io import StringIO
from django.http import HttpResponse

def home(request):
    return render(request, 'randomizer/home.html')

def property_list(request):
    properties = AhsPropertyLottery2.objects.all()
    return render(request, 'randomizer/property_list.html', {'properties': properties})

def applicant_list(request):
    applicants = ChAhsSubmissionsLottery2.objects.all().order_by('applicationid')
    return render(request, 'randomizer/applicant_list.html', {'applicants': applicants})

def run_lottery(request):
    if request.method == 'POST':
        property_id = request.POST.get('property_id')
        property = AhsPropertyLottery2.objects.get(propertyid=property_id)
        applicants = list(ChAhsSubmissionsLottery2.objects.all().order_by('applicationid'))
        random.shuffle(applicants)

        if property:
            property.lotterydate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            property.status = "Lottery Run"
            property.save()

        for idx, applicant in enumerate(applicants):
            applicant.lotteryposition = idx + 1
            applicant.save()

        # Generate the CSV file with detailed information
        csv_file = StringIO()
        writer = csv.writer(csv_file)
        writer.writerow([
            'ApplicationID', 'PropertyID', 'ApplicantName', 'Email', 'Development', 'Stage', 'SaveURL',
            'ApplicationURL', 'ResponseURL', 'UCRN', 'PropertyName', 'SubmitDate', 'Adults', 'Kids',
            'Joint', 'Nationality', 'Relationship', 'Household_Size', 'JointName', 'MortgageProvider',
            'Resident', 'Status', 'ResidentValid', 'IncomeValid', 'DepositValid', 'EquityValid',
            'MortgageAmount', 'HelpBuyAmount', 'Equity', 'Deposit', 'IncomeOverall', 'JointIncomeOverall',
            'HouseSizeValid', 'TaskURL', 'ParentID', 'Age', 'JointAge', 'County', 'InDublin', 'MortValid',
            'LotteryPosition', 'JointNationality', 'JointRelationship', 'JointEmail', 'AppealDate'
        ])

        for applicant in applicants:
            writer.writerow([
                applicant.applicationid,
                applicant.propertyid,
                applicant.applicantname,
                applicant.email,
                applicant.development,
                applicant.stage,
                applicant.saveurl,
                applicant.applicationurl,
                applicant.responseurl,
                applicant.ucrn,
                applicant.propertyname,
                applicant.submitdate,
                applicant.adults,
                applicant.kids,
                applicant.joint,
                applicant.nationality,
                applicant.relationship,
                applicant.household_size,
                applicant.jointname,
                applicant.mortgageprovider,
                applicant.resident,
                applicant.status,
                applicant.residentvalid,
                applicant.incomevalid,
                applicant.depositvalid,
                applicant.equityvalid,
                applicant.mortgageamount,
                applicant.helpbuyamount,
                applicant.equity,
                applicant.deposit,
                applicant.incomeoverall,
                applicant.jointincomeoverall,
                applicant.housesizevalid,
                applicant.taskurl,
                applicant.parentid,
                applicant.age,
                applicant.jointage,
                applicant.county,
                applicant.indublin,
                applicant.mortvalid,
                applicant.lotteryposition,
                applicant.jointnationality,
                applicant.jointrelationship,
                applicant.jointemail,
                applicant.appealdate
            ])

        # Send the email with the CSV file attached
        email = EmailMessage(
            'Your Property Allocation Results',
            'Please find attached the results of the property allocation.',
            'notkin2005@gmail.com',
            ['quamdeen.timson2@mail.dcu.ie'],
        )
        email.attach('allocations.csv', csv_file.getvalue(), 'text/csv')
        email.send()

        # Display the results on the web page with limited details
        return render(request, 'randomizer/lottery_result.html', {'applicants': applicants, 'property': property})
    return redirect('randomizer:home')
