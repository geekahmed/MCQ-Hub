import uuid
import requests
from bs4 import BeautifulSoup
from models import Category, SubCategory
import re
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
def get_all_categories(sanfoundry_main_url):
    page = requests.get(sanfoundry_main_url,headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')
    cat_links = soup.find_all('a')
    list_of_cats = []
    for link in cat_links:
        ll = link.get("href")
        ll_txt = link.getText()
        if "MCQs" in ll_txt:
            sub_categories = get_sub_categories(ll)
            # list_of_cats.append(Category(id=uuid.uuid4, name=ll_txt, sub_categories=sub_categories))

    # print(list_of_cats)


def get_sub_categories(link_of_category):
    page = requests.get(link_of_category,headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')
    sf_section = soup.find_all('div', class_='sf-section')
    title = ' '.join(sf_section[5].h2.getText().split()[1:])
    desc = sf_section[5].p.getText()
    # print(title)
    # print(desc)
    for l in sf_section[5].table.find_all('a'):
        print(l.getText())
        print(l.get('href'))


def get_questions(link):
    page = requests.get(link,headers = headers)
    soup = BeautifulSoup(page.content,'lxml')
    entry_content = soup.findAll('div',attrs={"class":"entry-content"})
    answers_and_expl = entry_content[0].find_all('div', class_='collapseomatic_content')
    questions = entry_content[0].find_all('p')

    ques_lst = []
    ans_lst = []
    exp_lst = []
    opt_ls = []

    for an in answers_and_expl:
        pass
    for bn in questions:
        
        qqa = re.findall(r"^(\d\d?. .*)\n" , bn.text)
        if qqa:
            ques_lst.append(str(qqa).replace("[" , "").replace("]" , "").replace("'" , ""))

        opt = re.findall(r"^[   ]?(\(?[a-z]\) .*)\n", bn.text)
        
        if opt:
            opt_ls.append(str(opt).replace("[" , "").replace("]" , "").replace("'" , ""))

    #print(questions[1].text)        
    #print(ques_lst)
    print(opt_ls)

    # print(re.findall(r"^(\d\d?. .*)\n" , tvb.find_all('p')[0].getText()))
    """
    [x.extract() for x in entry_content[0].findAll('div', class_='sf-mobile-ads')]
    [x.extract() for x in entry_content[0].findAll('div', class_='sf-desktop-ads')]    
    [x.extract() for x in entry_content[0].findAll('div', class_='desktop-content')]
    [x.extract() for x in entry_content[0].findAll('div', class_='mobile-content')]
    questions = entry_content[0].find_all('p')[1].getText()
    print(type(questions))
    ques_ls = []
    ques = re.findall(r"^(\d\d?. .*)\n" , questions)
    print(ques)
    # print(questions)
    """
    """
    for nn in questions.split('\n'):
        if "Explanation" in nn:
            print(nn)
    """

