# SpammerSpammer

This module is written so that you can spam a spammer. It has a few features:

1. SQL: <br>
 a. stores people you want to message,<br>
 b. stores messages that you want to end
  
2. MessageAPI that hijacks your phone and sends messages

3. Script that periodically sends spammers messages

[4. future: NLP thing to invent broken-english messages]

### Setup
1.  `export FLASK_APP=flaskr`
2.  `flask init-db`
3.  `flask run`

##### Schema
Technical details can be found in flaskr/schema.sql. But there are 6 tables:
- user; people
- post; --
- permission; who can send/do what
- messages; history of what was sent
- spammers; people who spam
- spam; junk. complete and utter junk
