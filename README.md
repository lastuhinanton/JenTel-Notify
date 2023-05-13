# JenTel-Notify

### Info:

Hello, my name is Anton and this is my project for making notification of Jenkins's status pipeline easier.

### Requirements:

1. **Jenkins** on any machines whatever you prefer
   (make sure that your Jenkins works well with the help of creating a Freestyle project, for example)
2. **Telegram bot**

## Start:

#### First let's create a Telegram bot:

Info: we do this because we need to get ***token_id*** and ***chat_id*** for our pipeline. In order to make it secured we will use Jenkins's credentials.

1. Open Telgram and type in the search field the exact write "@BotFather"

![1683978757759](image/README/1683978757759.png)

    Click on the first one with id**@BotFather**

2. Type "/start" and "/newbot" then folow the bot instructions untile the message like in the screenshoot below

   ![1683979251386](image/README/1683979251386.png)

   **Congratulations!** we have created a bot and also know the token of it. It will be usefull for us a little bit later.

   ![1683979465385](https://vscode-remote+ssh-002dremote-002blovedevops.vscode-resource.vscode-cdn.net/home/user/JenTel-Notify/image/README/1683979465385.png)
3. Now let's find out the chat_id and turn back to the search field writing @RawDataBot like in the screenshoot below

   ![1683979873200](image/README/1683979873200.png)
4. Click on the bot and click on the button "/start" and then we will see information about us. Take the special field -> "chat" -> "id".

   ![1683980362798](image/README/1683980362798.png)
5. Great! Now we know our id that we'll be used a little bit later.

#### Jenkins credentials:

   Now we should create credentials for Jenkins with this way
   ***Dashboard -> Manage Jenkins -> Credentials -> System -> Global credentials (unrestricted)***

   ![1683981081822](image/README/1683981081822.png)
6. Click on the button ***'+ Add Credentials'.***

   ![1683981185384](image/README/1683981185384.png)
7. Now we have to create 2 credentials with id ***"chat_id"*** and ***"bot_id"***.

* Create "***bot_id"*** credential taking token id in the red rectangle and put it the ***Secret*** field:
  ![1683981670899](image/README/1683981670899.png)

  ![1683981833152](image/README/1683981833152.png)
* Create new "***chat_id"*** credential taking token id in the red rectangle and put it the ***Secret*** field:
  ![1683980362798](image/README/1683980362798.png)

  ![1683982013708](image/README/1683982013708.png)

8. The final result like in the screenshoot below:

   ![1683982424183](image/README/1683982424183.png)

#### Connecting Python script into Jenkins pipeline

I assume that you already have a ready-made pipeline, but in any case, for now we can use the test one ([your_repo]/test/test.jenkins).

1. The configuration of this project is:

   ![1683984069145](image/README/1683984069145.png)

   ![1683984083882](image/README/1683984083882.png)
2. Let's take a look at the example below:

![1683982873806](image/README/1683982873806.png)

4. Our main part is like in the screenshoot below:

   ![1683983218987](image/README/1683983218987.png)

   What we have here:

   1. Credential 'chat_id' with variable 'CHAT_ID'.
   2. Credential 'bot_id' with variable 'BOT_ID'
