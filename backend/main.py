from citation import Citation
from summarizer import Summarizer
from reliability import Reliability

url = 'https://www.ibm.com/cloud/learn/what-is-artificial-intelligence'#'https://en.wikipedia.org/wiki/Artificial_intelligence'

Citation(url).main()
Summarizer(url).main()
date1 = Citation(url).date_finder()
Reliability(url, date1).main()