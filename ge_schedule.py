#!/usr/bin/python

import sys
from selenium import webdriver

RESHEDULE_COMMENT = 'earlier appointment opened up'
USERNAME = 'zyskowsk'
PASSWORD = 'Jussiisgod1!'
PHANTOMJS_PATH = '/usr/local/bin/phantomjs'

LOCATIONS = {
    'SFO': '5446',
    'SEA': '5420',
    'EWR': '5444',
    'JFK': '5140',
}

def schedule_for_location(location):
    browser = webdriver.Firefox()
    browser.get('https://goes-app.cbp.dhs.gov')
    browser.find_element_by_id('user').send_keys(USERNAME)
    browser.find_element_by_id('password').send_keys(PASSWORD)
    browser.find_element_by_id('SignIn').click()
    browser.get('https://goes-app.cbp.dhs.gov/main/goes/HomePagePreAction.do')
    browser.find_element_by_name('manageAptm').click()
    browser.find_element_by_name('reschedule').click()
    select = browser.find_element_by_id('selectedEnrollmentCenter')
    for option in select.find_elements_by_tag_name('option'):
        if option.get_attribute('value') == LOCATIONS[location]:
            option.click()
    browser.find_element_by_name('next').click()
    browser.find_elements_by_class_name('entry')[0].click()
    browser.find_element_by_name('comments').send_keys(RESHEDULE_COMMENT)
    browser.find_element_by_name('Confirm').click()

schedule_for_location(sys.argv[1])
