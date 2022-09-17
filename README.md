# Twitter-App

**Team Name** : Spartan Devs

**Team Members**: Bhavya Hegde, Darshini Venkatesha Murthy Nag, Sirisha Polisetty.

## Problem Statement: 
1. Develop a simple twitter service that implement any Twitter API to to programmatically create, retrieve and delete a Tweet
2. Develop a simple Web UI that  implements your service and demonstrates the functions.

## Twitter Developer Account Setup 

**Step 1**: Created a Project name PROJECT1 in Twitter Developer Platform and created an app named it as artemis_twitter_api.

**Step 2**: Setup the app with the following setting to enable us to read, write and retrieve from twitter.
- App Permissions :  read and write tweets on twitter.
- Type of App : Web App, Automated App or Bot
- App Info:
  - Callback URL : https://www.twitter.com
  - Website URL : https://www.twitter.com 

**Step 3**: Securely Stored the required keys for the project setup in our service.
Consumer Key and Secret, Access Token and Secret.

## Implementation Steps:

**Step 1** : Using the keys we have created in Step above from developer.twitter.com. We have developed a django application using python.
Our  web application would support the following features

Post a Tweet, Delete a Tweet, Retrieve Tweets

**Step 2**: Enter the tweet to be posted and Click on submit button.
On click of submit Tweet is successfully posted and the link to the tweet is shown in the UI.

**Step 3** : Delete tweet using tweet_id
Enter the tweet_id to be deleted.
On click of submit button, the tweet is deleted successfully and a message is displayed in UI.

**Step 4** : Retrieve Tweet
Enter the search keyword to retrieve tweets for that keyword. On click of submit button  list of tweets is displayed. 

## Testing Setup Details:
We have used the python unittest framework as our codebase is in python django.
We have written unit test cases to cover the following methods

- Website response
- Tweet post
- Tweet delete
- Tweet retrieve.

## How to Run the Twitter App

Setup the following keys in twitter/settings.py
```
API_KEY='..'
API_KEY_SECRET='..'
ACCESS_TOKEN='..'
ACCESS_TOKEN_SECRET='..'
BEARER_TOKEN = '..'
```

## Install python Dependencies for django app

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

go to http://localhost:8000
```