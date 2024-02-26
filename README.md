# Health-Care-Chatbot

<img src="https://www.scnsoft.com/blog-pictures/healthcare/how-chatbots-and-ai-are-changing-the-healthcare-industry_1.png">

    This chatbot will provide quick answers to FAQs by setting up rule-based keyword chatbots 
    with ¨if/then¨ logic. This chatbot will use a series of well-defined rules  to guide 
    customers through a series of menu options that can help answer their questions. 
    It will be there for customers 24/7 on their preferred channels, and simultaneously 
    handle more queries at once. 



<img src="https://miro.medium.com/max/875/1*69vLXZCjrJwdXytj0CTSiQ.jpeg">
PS: Please do not forget to drop a star if you like it!

# Install Guide
version: python 3.10.5
py -m pip install --upgrade pip

py -m pip install openai==0.27.8
py -m pip install flask
py -m pip install cors
py -m pip install flast_cors
py -m pip uninstall langchain
py -m pip install langchain==0.0.240
py -m pip install python-dotenv
py -m pip install gradio
py -m pip install gpt_index
py -m pip install dote
py -m pip install twilio

# server installation
-for linux
py -m pip install gunicorn
-for windows
py -m pip install waitress
# Python Run
python run.py runserver 0.0.0.0:3000