from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

def reliability_scorer():
    suffix_outof = 1
    testURL = "https://libguides.uwgb.gov/"

    suffixes = {
        ".edu": suffix_outof,
        ".gov": suffix_outof,
        ".org": suffix_outof,
        ".gov.ca": suffix_outof,
        ".ca": suffix_outof/2,
        ".com": suffix_outof/2,
        ".net": suffix_outof/2
    }

    pDate = "2022-09-22" #article published date
    current_date = date.today()
    formattedDate = datetime.strptime(pDate, '%Y-%m-%d').date() #convert string to date object, remove if not needed 

    suffix_score = -1
    #Suffix scorer
    for value in suffixes:
        if value in testURL:
            suffix_score = suffixes[value]
            break
        else:
            suffix_score = 0
    print("suffix score:", suffix_score)

    security_score = -1
    #"Security" scorer
    if testURL[:5] == "https":
        security_score = 1
    else:
        security_score = 0
    print("security score:", security_score)

    #Data scorer
    date_score = -1
    years10 = current_date - relativedelta(years=10)
    years5 = current_date - relativedelta(years=5)
    years2 = current_date - relativedelta(years=2)
    years1 = current_date - relativedelta(years=1)

    if (formattedDate <= years10):
        date_score = 0
    elif (formattedDate> years10 and formattedDate<= years5):
        date_score = 1
    elif (formattedDate> years5 and formattedDate<= years2):
        date_score = 4
    elif (formattedDate> years2 and formattedDate<= years1):
        date_score = 7
    elif (formattedDate>years1):
        date_score = 10
    print("date score:", date_score)

    #Final reliability score
    reliability_score = ((suffix_score*10) + (security_score*10) + (date_score)) / 3
    print("reliability score", reliability_score)

reliability_scorer()
