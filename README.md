# AnonUS_bot
Telegram Bot for AnonUS (Anonymous URL shortner)

## Deploy on heroku

- Create heroku account and install heroku-cli, git on your machine.

- Clone/Download this repo.

- remove this repo origin using git
    ```
    git remote remove origin
    ```

- Login to heroku account and create new app
    ```
    heroku login
    ```

    ```
    heroku create app-name
    ```

- add heroku git link to the cloned repo
    ```
    heroku git:remote -a app-name
    ```

- Update Telegram bot api token and url link with heroku app
    ```python
    TOKEN = "<telegram-bot-api-token>"
    ```
    ```python
    bot.set_webhook(url='https://app-name.herokuapp.com/'+TOKEN)
    ```

- add files, commit changes, and push commit.
    ```
    git add .
    git commit -m "changes for heroku deployment"
    git push heroku
    ```

- Test your bot.
