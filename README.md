# openai-test-bot

This is a very basic Python bot that uses OpenAI API to query the PyTorch website.
You can modify the script to query any other website. This is a very simple example just to get a taste of
how easy it is to use OpenAI API. This example is inspired by the [OpenAI documentation](https://platform.openai.com/docs/quickstart). 

https://user-images.githubusercontent.com/5317992/233195802-79ba44e8-4d5d-4ffe-b9e8-690ce7d0d79c.mov

# Prerequisites

* A GitHub Account
* An Open AI token (can be obtained in your Open AI Account Settings)

# How to use

You can run this as a script or use the notebook instead. To learn how to run the notebook, see 

1. Fork this repo by clicking [Fork](https://github.com/svekars/openai-test-bot/fork) in the upper-right corner of the home page.
2. One your computer, open a terminal.
3. Clone your fork to your computer by running:


   If you are using SSH:
   
   ```
   git clone git@github.com:<path to your fork>.git
   ```
   
   If you are using HTTPs: 
   
   ```
   git clone https://github.com/<path-to-your-fork>.git
   ```
   
4. Change directory to your fork:

   ```
   cd path-to-your-fork
   ```

6. Install dependencies: 

   ```
   pip3 install -r requirements.txt
   ```
   
8. Open the script file for editing, for example using `vim`:

   ```
   vi qa-bot-test.py
   ```

8. In the script, replace `YOUR_API_KEY` with the token you have obtained from your OpenAI account. 
9. Save the file: 
   
   ```
   :x! 
   ```

11. Run the script:

   ```
   python3 qa-bot-test.py
   ```
   
   Response:
   
   ```
   What would you like to learn? (type "exit" to quit):
   ```
   
8. Type your question and receive an answer. For example: How to install PyTorch?
9. To terminate the bot, type ``exit``.

# Running as a Jupyter Noebook

We have a Jupyter notebook in addition to Python script that you can test. You need to have Jupyter labs installed. You can install it by running the following command:

```
pip install jupyterlab
pip install notebook
```

After that, navigate to the directory of this repo and run:

```
jupyter notebook
```

This opens the Jupyter labs UI in your browser from where you can select the `qa-bot-test.ipynb` notebook to open in a new window.
Run all the cells in the notebook one after another and ask the bot questions as needed.
After you are done, go back to the terminal and click *CTRL-D* to interrupt the process.

Here is a quick demo of how it works:

https://user-images.githubusercontent.com/5317992/235981225-9cda5b12-8d83-4452-b628-1fbe1622f1a7.mp4

# Troubleshooting

```
openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.
```

If you see the error above, it means exactly that - you have execeed your current limit and need to either wait or
upgrade your account.
