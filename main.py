import datetime
from selenium import webdriver

RESHEDULE_COMMENT = 'earlier appointment opened up'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
PHANTOMJS_PATH = '/usr/local/bin/phantomjs'
RESERVE = True

LOCATIONS = {
    'SFO': '5446',
    'SEA': '5420',
    'EWR': '5444',
    'JFK': '5140',
}

def print_date_for_location(location, location_value):
    browser = webdriver.PhantomJS(PHANTOMJS_PATH)
    #browser = webdriver.Firefox()
    browser.get('https://goes-app.cbp.dhs.gov')
    browser.find_element_by_id('user').send_keys(USERNAME)
    browser.find_element_by_id('password').send_keys(PASSWORD)
    browser.find_element_by_id('SignIn').click()
    browser.get('https://goes-app.cbp.dhs.gov/main/goes/HomePagePreAction.do')
    browser.find_element_by_name('manageAptm').click()
    browser.find_element_by_name('reschedule').click()
    select = browser.find_element_by_id('selectedEnrollmentCenter')
    for option in select.find_elements_by_tag_name('option'):
        if option.get_attribute('value') == location_value:
            option.click()
    browser.find_element_by_name('next').click()
    day = browser.find_element_by_css_selector('td.header .date tbody td:first-child').text
    month_year = browser.find_element_by_css_selector('td.header .date tbody tr:nth-child(2)').text
    month, year = month_year.split(', ')

    sfo_reserved = False
    if RESERVE:
        if location == 'SFO' and (month == 'March' and day in [29, 31]):
            browser.find_elements_by_class_name('entry')[0].click()
            browser.find_element_by_name('comments').send_keys(RESHEDULE_COMMENT)
            browser.find_element_by_name('Confirm').click()
            sfo_reserved = True
    browser.close()

    if sfo_reserved:
        print '%s: %s %s, %s RESERVED' % (location, day, month, year)
    else:
        print '%s: %s %s, %s' % (location, day, month, year)

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print '---------------------------------------------'
for location, value in LOCATIONS.iteritems():
    print_date_for_location(location, value)
print '---------------------------------------------'
print
