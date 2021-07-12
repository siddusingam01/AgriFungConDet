# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:43:53 2020

import datetime
@author: chait 
"""
import selenium
import time
import os
# Using Chrome to access web]
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
# Open the website
driver.get('https://accounts.adafruit.com/users/sign_in')
wait= WebDriverWait(driver,10)
#time.sleep(5)
# Select the id box
id_box = driver.find_element_by_name('user[login]')
#id_box.send_keys('S_V_S_Siddartha')
id_box.send_keys('jayaprakash72')
# Find password box
pass_box = driver.find_element_by_name('user[password]')
# Send password
#pass_box.send_keys('$iddu2001')
pass_box.send_keys('jayaprakash')
# Find login button
login_button = driver.find_element_by_name('commit')
# Click login
login_button.click()
driver.get('https://io.adafruit.com/jayaprakash72/dashboards')
#driver.get('https://io.adafruit.com/S_V_S_Siddartha/feeds')
#feed_button=driver.find_element_by_class_name('dropdown-label')#& (driver.find_element_by_link_text('Feeds')))
#feed_button.click()
time.sleep(10)
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--remote-debugging-port=9222")
driver.get('https://io.adafruit.com/jayaprakash72/feeds')
time.sleep(10)
driver.get('https://io.adafruit.com/jayaprakash72/feeds/mois')
#dowm_button=driver.find_element_by_link_text('Download All Data')
#dowm_button.click()
time.sleep(10) 
#driver.get('https://adafruit-io-production.s3.us-east-1.amazonaws.com/downloads/compressed_files/000/023/026/original/data20200312-17383-358oq7.csv?response-content-disposition=attachment%3B%20filename%3D%22mois-20200312-1620.csv%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJ4DKLO7S5KP5G4LA%2F20200312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200312T162405Z&X-Amz-Expires=65&X-Amz-SignedHeaders=host&X-Amz-Signature=07a4084c027edc773280a031434dde80dcdbdfe0fe4d665d882b5283617da22b')
down_button=driver.find_element_by_xpath("//*[@id='content-wrapper']/div[2]/div/div[2]/div[1]/a[2]/span")
down_button.click()
time.sleep(5)
#down_csv_button=driver.find_element_by_xpath("//*[@id='aio-key-modal']/div/div/div[2]/p[2]/button[2]")
#down_csv_button.click()
down_json_button=driver.find_element_by_xpath("//*[@id='aio-key-modal']/div/div/div[2]/p[2]/button[1]")
down_json_button.click()
time.sleep(5)
link_button=driver.find_element_by_xpath("//*[@id='aio-key-modal']/div/div/div[2]/div/table/tbody/tr[1]/td[1]/a")
link_button.click()
#root_button=driver.find_element_by_xpath("//a[@class_name='btn blue btn btn-default'][@type='button'][@tag_name='button'][@link_text='Download as CSV']")
#root_button.click()
#root_button=driver.find_element_by_class_name('fa fa-bars')
#out_button=driver.find_element_by_id('outer-wrapper')
#out_button.click()
#in_button=driver.find_element_by_id('innner-wrapper')
#in_button.click()
#driver.get('https://adafruit-io-production.s3.us-east-1.amazonaws.com/downloads/compressed_files/000/023/026/original/data20200312-17383-358oq7.csv?response-content-disposition=attachment%3B%20filename%3D%22mois-20200312-1620.csv%22&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAJ4DKLO7S5KP5G4LA%2F20200313%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20200313T053310Z&amp;X-Amz-Expires=65&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7cb99ab220b2e74dd38ee8bbaa9fbb711778f29345b79a2ff723ec2714c7fe82')
#driver.get('https://adafruit-io-production.s3.us-east-1.amazonws.com/downloads/compressed_files/000/023/026/original/data20200312-17383-358oq7.csv?response-content-disposition=attachment%3B%20filename%3D%22mois-20200312-1620.csv%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJ4DKLO7S5KP5G4LA%2F20200313%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200313T053310Z&X-Amz-Expires=65&X-Amz-SignedHeaders=host&X-Amz-Signature=7cb99ab220b2e74dd38ee8bbaa9fbb711778f29345b79a2ff723ec2714c7fe82')