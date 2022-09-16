
#import unittest

#from django.http import HttpResponse
from django.test import TestCase, RequestFactory
from .views import index
import datetime
import time
import re

# Create your tests here.



### Darshini Venkatesha Murthy Nag Contribution###

class ViewsTestCase(TestCase):
   
    def test_index_loads_properly(self):
        print("Running test to check if the website is responsponding")
        response=self.client.get('http://127.0.0.1:8000')
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        print("Test Successful")

        #Bhavya Hegde's Contribution#

     
    def test_index_create(self):
        self.factory = RequestFactory()
        print("Test to check if the tweet is posted to the feed")
        request = self.factory.post('',{"content":"posting some new unit test tweet: "+str(datetime.datetime.now())})
        response = index(request)
        print(response)
        self.assertEqual(response.status_code, 200)
        print("Test successful")

        ## Darshini Venkatesha Murthy Nag Contribution##

    def test_index_delete(self):
        time.sleep(5)
        self.factory=RequestFactory()
        request = self.factory.post('',{"content":"Delete unit test tweet: "+str(datetime.datetime.now())})
        response = index(request)
        #print(response)
        #print(response.content)
        #print(response.context)
        match_string = re.search("\/status\/[0-9].*\"",response.content.decode('utf-8'))
        tmp_id = match_string[0].split("/")[2].split("\"")[0]
        time.sleep(5)
        request= self.factory.post('',{"ID":str(tmp_id)})
        response=index(request)
        print("Tweet Deleted!")
        #print(response)
        self.assertEqual(response.url, "delete.html")
        print("Test to delete tweets successful")

        ## Sirisha Polisetty Contribution ##

    def test_getQuery(self):
        self.factory = RequestFactory()
        print("Test to check if we are able to retrieve tweets as expected")
        request = self.factory.post('',{"getQuery":"Dogs"})
        response = index(request)
        #print(response)
        #print(response.content)
        total_count = len(re.findall("\<li\>",response.content.decode('utf-8')))
        self.assertTrue(total_count>0)
        print("Tweets retrived successfully, test successful")






