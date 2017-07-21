import mechanize
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time
#read in the file of roll numbers
df = pd.read_excel("")
df1 = df.ix[:,0:1]
for x in range(len(df1.index)):
    print df1['number'].iloc[x]
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    r = br.open('http://keapu-webugpp01-in.cloudapp.net/results2017_r2p/main/results.php')
    time.sleep(1)
    html = r.read()
    time.sleep(1)
    rollno = df1['number'].iloc[x]
    def select_form(form):
        return form.attrs.get('action', None) == 'resultscheck.php'
    br.select_form(predicate=select_form)
    #br.form.find_control('control_name').readonly = False
    br.form['txtrollno'] = rollno
    req = br.submit()
    time.sleep(2)
    html = req.read()
    parsed_html = BeautifulSoup(html)
    parsed_html.prettify()
    parsed_table = parsed_html.body.find('table', attrs={'height':'200'})
    if parsed_table == None:
        candidate_info = "NoSeat"
    else:
    #print [tr.find('td').text for tr in parsed_table.findAll('tr')]
        candidate_info = [tr.findAll('td')[-1].text for tr in parsed_table.findAll('tr')]
    #print type(candidate_info)
    f= open('cetscraped6.csv', 'a') 
    for word in candidate_info:
        f.write(word)
    time.sleep(1)
with open('cetscraped.txt', 'w') as f:
    f.write(req.read())
    f.close()
