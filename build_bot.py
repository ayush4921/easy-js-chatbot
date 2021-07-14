from jinja2 import Template
import json
import os


intents_json_url = os.path.join(
    os.getcwd(), "templates", "editable_template.json")
html_body_url = os.path.join(os.getcwd(), "templates", "chat_bot.html")
html_head_url = os.path.join(os.getcwd(), "templates", "chat_bot_head.html")
javascript_template = os.path.join(
    os.getcwd(), "templates", "chat_bot_template.js")
css_template_url = os.path.join(
    os.getcwd(), "templates", "chat_bot_css.css")
bot_template = json.loads(open(intents_json_url).read())
name_of_the_bot = bot_template["details_of_bot"]["name_of_the_bot"]
image_url_of_avatar = bot_template["details_of_bot"]["image_url_of_avatar"]
image_url_of_chatbot = bot_template["details_of_bot"]["image_url_of_chatbot"]
position_of_chatbot = bot_template["details_of_bot"]["position"]
to_open_on_load = bot_template["details_of_bot"]["open_on_load"]

if to_open_on_load:
    load_on_open = "$(document).ready(openElement);"
else:
    load_on_open = ""

intents_to_be_put_in_js = json.dumps(bot_template["intents"])


with open(html_body_url, 'r') as f:
    html_body_string = Template(f.read())


with open(html_head_url, 'r') as f:
    html_body_head = Template(f.read())

with open(css_template_url, 'r') as f:
    css_template = Template(f.read())


css_template = css_template.render(
    image_url_of_chatbot=image_url_of_chatbot, image_url_of_avatar=image_url_of_avatar, position_of_chatbot=position_of_chatbot)

html_body_string = html_body_string.render(css_template=css_template,
                                           name_of_the_bot=name_of_the_bot)

html_body_head = html_body_head.render()

with open(javascript_template, 'r') as f:
    js_text = Template(f.read())

with open("chat_bot_final.js", 'w') as f:
    js_text = js_text.render(
        html_body_string=html_body_string, html_body_head=html_body_head, intents_to_be_put_in_js=intents_to_be_put_in_js, load_on_open=load_on_open)
    f.write(js_text)
