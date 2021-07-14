# Easy JS Auto Embed Chatbot

  - [How to make your own chat bot and place it in a website](#how-to-make-your-own-chat-bot-and-place-it-in-a-website)
  - [How it works](#how-it-works)
  - [Technical details](#technical-details)


## How to make your own chat bot and place it in a website:
---
#### 1) Edit `templates\editable_template.json` file with the details of your chatbot.  

#### 2) Check if python is installed in your system  

#### 3) Install the requirements by running "pip install -r requirements.txt"  

#### 4) Run `build_bot.py  `

#### 5) You should see a file called `chat_bot_final.js`

#### 6) Copy the last three script tags and place them at the end of your website along with the chat_bot_final javascipt file. (or host the javascript file and change the src of the last script tag)

```

<script src="https://cdn.jsdelivr.net/npm/fuse.js/dist/fuse.js"></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script src="./chat_bot_final.js"></script>

```
## How it works?
---
The questions you place in the `templates\editable_template.json` will be checked for similarity with the phrase that user puts in chatbot using the fuse.js library. The most relevant question will then be selected and a response will be randomly selected from the responses list provided for the question.
\
&nbsp;
## Technical details:
---
The javascript templated will be populated with the html which will be placed in the head and the body target of the webpage where you are going to install the chatbot. 

A style tag will be inserted in your website's head for the css of the chatbot.

You can edit the css in `templates\chat_bot_css.css` to change the look of the chatbot.
\
&nbsp;
## How it looks:
![easy_chat_bot](https://user-images.githubusercontent.com/62711517/125550594-ee544479-2da0-478d-9ca9-b39a44a37e79.png)
![11](https://user-images.githubusercontent.com/62711517/125550605-074191d1-1155-4d88-b0c7-c699861a817f.png)
![abc](https://user-images.githubusercontent.com/62711517/125550612-50a46e3f-4231-4b7e-8bf5-84d8a7f43eab.png)
