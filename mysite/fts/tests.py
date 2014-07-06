import time

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PollsTest(LiveServerTestCase):
    fixtures = ['auth.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn("Django administration", body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')

        password_field.send_keys(Keys.ENTER)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn("Site administration", body.text)

        poll_links = self.browser.find_elements_by_link_text("Polls")
        self.assertEquals(len(poll_links), 2)

        poll_links[1].click()

        self.browser.find_element_by_link_text("Add poll").click()

        self.fail("finish me!")

# Create your tests here.
