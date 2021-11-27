import time
import datetime
from persiantools.jdatetime import JalaliDate
import hijri_converter
from hijri_converter import Hijri, Gregorian
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
import math
import mysql.connector as msql
from mysql.connector import Error
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def crawl_to_mainpage():
    main_page = driver.get('https://www.tgju.org/')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="popup-layer-container"]/div[2]/a').click()

def crawl_dollorcurrency():
    dollors_page = driver.find_element_by_xpath('//*[@id="l-price_dollar_rl"]').click()
    time.sleep(2)
    dollor_page = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[1]/div/div/div[1]/table/tbody/tr[1]/th').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_ons():
    dollors_page = driver.find_element_by_xpath('//*[@id="l-ons"]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_mesgal():
    dollors_page = driver.find_element_by_xpath(' //*[@id="l-mesghal"]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_gold18():
    dollors_page = driver.find_element_by_xpath('//*[@id="l-geram18"]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_gold24():
    dollors_page = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div[3]/div[2]/table/tbody/tr[2]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_emami_coin():
    dollors_page = driver.find_element_by_xpath('//*[@id="coin-table"]/tbody/tr[1]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_azadi_coin():
    dollors_page = driver.find_element_by_xpath('//*[@id="coin-table"]/tbody/tr[2]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_nim_coin():
    dollors_page = driver.find_element_by_xpath('//*[@id="coin-table"]/tbody/tr[3]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_rob_coin():
    dollors_page = driver.find_element_by_xpath('//*[@id="coin-table"]/tbody/tr[4]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

def crawl_gerami_coin():
    dollors_page = driver.find_element_by_xpath('//*[@id="coin-table"]/tbody/tr[5]').click()
    time.sleep(2)
    dollor_history_page = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)


def switch_commodit(argument):
    switcher = {
        "دلار": 1,
        "انس طلا": 2,
        "مثقال طلا": 3,
        "طلای 18 عیار / 750": 4,
        "طلای ۲۴ عیار": 5,
        "سکه امامی": 6,
        "سکه بهار آزادی": 7,
        "نیم سکه": 8,
         "ربع سکه": 9,
        "سکه گرمی": 10
    }
    return switcher.get(argument, "Invalid name")


def scrape_currency(row_num):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    dom = etree.HTML(str(soup))

    #name
    name_xpath = '//*[@id="main"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/h1'
    name = driver.find_element_by_xpath(name_xpath).text
    print(name)

    #commodit
    commodit = switch_commodit(name)
    print(commodit)


    #shamsidate
    shamsi_date_xpath = '//*[@id="table-list"]/tr['
    shamsi_date_xpath += str(row_num)
    shamsi_date_xpath += ']/td[8]'
    shamsi_date = driver.find_element_by_xpath(shamsi_date_xpath).text
    shamsi_year, shamsi_month, shamsi_day = (int(x) for x in shamsi_date.split('/'))
    shamsi_day_of_year = JalaliDate(shamsi_year, shamsi_month, shamsi_day).strftime('%j')
    shamsi_day_of_week = JalaliDate(shamsi_year, shamsi_month, shamsi_day).strftime('%w')
    if '/' in shamsi_date:
        shamsi_date = shamsi_date.replace('/', '')


    #miladidate
    miladi_date_xpath = '//*[@id="table-list"]/tr['
    miladi_date_xpath += str(row_num)
    miladi_date_xpath += ']/td[7]'
    miladi_date = driver.find_element_by_xpath(miladi_date_xpath).text
    year, month, day = (int(x) for x in miladi_date.split('/'))
    ans = datetime.date(year, month, day)
    miladi_day_of_year = ans.strftime('%j')
    miladi_day_of_week = ans.strftime('%w')
    if '/' in miladi_date:
        miladi_date = miladi_date.replace('/', '')

    hijri_date = Gregorian(year, month, day).to_hijri()
    hijri_day_of_week = hijri_date.weekday()
    hijri_date = str(hijri_date)
    hijri_day_of_week = str(hijri_day_of_week)
    if '-' in hijri_date:
        hijri_date = hijri_date.replace('-', '')


    #open
    open_xpath = '//*[@id="table-list"]/tr['
    open_xpath += str(row_num)
    open_xpath += ']/td[1]'
    open = driver.find_element_by_xpath(open_xpath).text

    #low
    low_xpath = '//*[@id="table-list"]/tr['
    low_xpath += str(row_num)
    low_xpath += ']/td[2]'
    low = driver.find_element_by_xpath(low_xpath).text

    #high
    high_xpath = '//*[@id="table-list"]/tr['
    high_xpath += str(row_num)
    high_xpath += ']/td[3]'
    high = driver.find_element_by_xpath(high_xpath).text

    #close
    close_xpath = '//*[@id="table-list"]/tr['
    close_xpath += str(row_num)
    close_xpath += ']/td[4]'
    close = driver.find_element_by_xpath(close_xpath).text
    insert_to_database(commodit, name, shamsi_date, miladi_date, hijri_date, miladi_day_of_week, miladi_day_of_year,shamsi_day_of_week,shamsi_day_of_year,hijri_day_of_week, open, low, high, close )


def scrape_rows():
    for x in range(1, 31):
        scrape_currency(row_num=x)


def crawl_scrape_all():
    first_number = 1
    last_number_string = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[6]').text
    last_number = int(last_number_string)
    print(last_number)
    current_number = 1
    page_elements = driver.find_elements_by_class_name("paginate_button")
    time.sleep(8)
    driver.find_element_by_xpath("/html/body/div[15]/i").click()
    driver.find_element_by_xpath("/html/body/div[14]/i").click()
    while current_number < last_number:
        time.sleep(2)
        scrape_rows()
        current_number += 1
        current_number_string = str(current_number)
        page_elements = driver.find_elements_by_class_name("paginate_button ")
        next_page = [x for x in page_elements if current_number_string == x.text][0]
        next_page.click()
        time.sleep(1)


def crawl_scrape_dollor():

    crawl_to_mainpage()
    crawl_dollorcurrency()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_ons():

    crawl_to_mainpage()
    crawl_ons()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_mesgal():

    crawl_to_mainpage()
    crawl_mesgal()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_gold18():

    crawl_to_mainpage()
    crawl_gold18()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_gold24():

    crawl_to_mainpage()
    crawl_gold24()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_emami():

    crawl_to_mainpage()
    crawl_emami_coin()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_azadi():

    crawl_to_mainpage()
    crawl_azadi_coin()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_nim():

    crawl_to_mainpage()
    crawl_nim_coin()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_rob():

    crawl_to_mainpage()
    crawl_rob_coin()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def crawl_scrape_gerami():

    crawl_to_mainpage()
    crawl_gerami_coin()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[2]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    crawl_scrape_all()


def create_database():
    query1 = " CREATE DATABASE IF NOT EXISTS Currency "
    #  query2 = " CREATE TABLE IF NOT EXISTS currencyinfo(name varchar(255) PRIMARY key, companycode varchar(255),12code varchar(255)  ) "
    query3 = " CREATE TABLE IF NOT EXISTS currency(Commodit int, Name varchar(255) ,Shamsi_date varchar(255), Miladi_date varchar(255), Hijri_date varchar (255)," \
             "MiladiDayofWeek varchar(255) ,MiladiDayofYear varchar(255) ,ShamsiDayofWeek varchar(255) ,ShamsiDayofYear varchar(255) ,HijriDayofWeek varchar(255) ," \
             "Open varchar(255) ,Low varchar(255),High varchar(255), Close varchar(255), PRIMARY KEY (Shamsi_date ,Name)) "
    try:
        conn = msql.connect(host='localhost', user='root', password='13772010')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query1)
            print("Database is created")
    except Error as e:
        print("Error while connecting to MySQL", e)

    try:
        conn = msql.connect(host='localhost', database='Currency', user='root', password='13772010')
        if conn.is_connected():
            cursor = conn.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            print('Creating table....')
            # cursor.execute(query2)
            cursor.execute(query3)
            print("Tables are created....")

    except Error as e:
        print("Error while connecting to MySQL", e)


def insert_to_database(Commodit, Name, Shamsi_date, Miladi_date, Hijri_date, Miladi_Day_of_week, Miladi_Day_of_year, Shamsi_Day_of_week, Shamsi_Day_of_year, Hijri_Day_of_week , Open, Low, High, Close):
    data = {
        "Commodit": Commodit,
        "Name": Name,
        "ShamsiDate": Shamsi_date,
        "MiladiDate": Miladi_date,
        "HijriDate": Hijri_date,
        "MiladiDayofWeek": Miladi_Day_of_week,
        "MiladiDayofYear": Miladi_Day_of_year,
        "ShamsiDayofWeek": Shamsi_Day_of_week,
        "ShamsiDayofYear": Shamsi_Day_of_year,
        "HijriDayofWeek": Hijri_Day_of_week,
        "Open": Open,
        "Low": Low,
        "High": High,
        "Close": Close
    }
    condition_query1 = " SELECT * FROM Currency.Currency WHERE name = %s and shamsi_date = %s "
    insertion_query1 = " INSERT INTO Currency.currency VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

    data_f_s = pd.DataFrame(data, index=[0])
    print(data_f_s)
    try:
        conn = msql.connect(host='localhost', database='Stocks', user='root', password='13772010')
        if conn.is_connected():
            cursor = conn.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            cursor.execute(condition_query1, (Name, Shamsi_date))
            count = cursor.rowcount
            if count == 0:
                cursor.execute(insertion_query1, (Commodit, Name, Shamsi_date, Miladi_date, Hijri_date, Miladi_Day_of_week, Miladi_Day_of_year, Shamsi_Day_of_week, Shamsi_Day_of_year, Hijri_Day_of_week, Open, Low, High, Close))
                print("inserted")
            else:
                quit()
            conn.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)

    return data_f_s


def get_excel():

    query3 = " SELECT * FROM Currency.currency"
    try:
        conn = msql.connect(host='localhost', database='Currency', user='root', password='13772010')
        if conn.is_connected():
            cursor = conn.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            cursor.execute(query3)
            rows = cursor.fetchall()
            data = pd.DataFrame(rows,
                                columns=['Commodit', 'Name', 'Shamsi_date', 'Miladi_date', 'Hijri_date', 'Miladi_Day_of_week', 'Miladi_Day_of_year',
                                         'Shamsi_Day_of_week', 'Shamsi_Day_of_year', 'Hijri_Day_of_week', 'Open', 'Low','High', 'Close'])
            conn.commit()
            filename_needed = 'C:/Users/aidin/Downloads/dataset.csv'
            data.to_csv(filename_needed, index=False, header=True, encoding="utf-8")
    except Error as e:
        print("Error while connecting to MySQL", e)


crawl_scrape_dollor()

