# KahootOrNotToKahoot
Discord bot that will automate logging into polls and answer questions if you have not selected an answer

## Set Up
1. Clone the repo onto your machine.
2. [Create and get your discord server token.](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)
3. [Put the token in a .env file.](https://realpython.com/how-to-make-a-discord-bot-python/#interacting-with-discord-apis) 
4. Install the required dependacies in ```requirments.txt``` using ```python3 -m pip install -r python-requirements.txt``` then run ```        python3 botwithkahoot.py        ```. If done correctly, you should see a confirmation in the terminal.
5. Now, in the Discord server use the command ```        !pin=        ``` with the Kahoot game pin you want. Happy Kahooting!
6. You can follow this [tutorial](https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz) to keep the python bot always running.
## Road Blocks
-   No public facing Kahoot API
-   we have never programmed our own discord bots
- kahoot dynamically loads elements so python modules like beautiful dont work bythem selves
