from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

class Reliability():
    def __init__(self, url, date1):
        self.url = url
        self.date1 = date1
    def main(self):
        reliability = self.reliability_scorer()
        return reliability
    def reliability_scorer(self):
        suffix_outof = 1

        suffixes = {
            ".edu": suffix_outof,
            ".gov": suffix_outof,
            ".org": suffix_outof,
            ".gov.ca": suffix_outof,
            ".ca": suffix_outof/2,
            ".com": suffix_outof/2,
            ".net": suffix_outof/2
        }


        #WIKIPEDIA SPECIAL SCORE
        if "wikipedia" in self.url:
            return 6.0
        elif "sex" in self.url:
            return 6.9

        #date1 = "2022-09-22" #article published date
        current_date = date.today()
        formattedDate = datetime.strptime(self.date1, '%Y-%m-%d').date() #convert string to date object, remove if not needed 

        suffix_score = -1
        #Suffix scorer
        for value in suffixes:
            if value in self.url:
                suffix_score = suffixes[value]
                break
            else:
                suffix_score = 0
        #print("suffix score:", suffix_score)

        security_score = -1
        #"Security" scorer
        if self.url[:5] == "https":
            security_score = 1
        else:
            security_score = 0
        #print("security score:", security_score)

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
        #print("date score:", date_score)

        #Final reliability score

        reliability_score = round(((suffix_score*10) + (security_score*10) + (date_score)) / 3,2)
        #print("reliability score", reliability_score)
        #SPECIAL USE CASE
        if security_score == 0:
            return round(reliability_score / 2,2)

        return reliability_score
