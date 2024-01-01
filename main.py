import telebot
import logging
import math

# Replace 'YOUR_BOT_TOKEN' with the actual token you get from BotFather on Telegram
TOKEN = '5965168157:AAHzgqx8nOhcBFGtwTK6ZqUbZfDkIoq9BlM'

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = telebot.TeleBot(TOKEN)
print("Bot Connected..")

@bot.message_handler(commands=['start', 'help'])
def handle_help(message):
    help_message = (
        'Welcome to the Team OVR Calculator!\n\n'
        'Instructions:\n'
        '1. Send your total base OVRs and total ranks in a single message, separated by a space.\n'
        '   For example: `985 46`\n\n'
        '2. The bot will calculate your Team OVR and provide next upgrade information.\n\n'
        'Terms Explanation:\n'
        ' - Team OVR: Average Base OVR (rounded up) + Average Rank (rounded up)\n'
        ' - Base OVR: Player\'s base OVR, excluding Training/Rank (if any)\n'
        ' - Rank: Number of ranks in the team (deduct the base OVR of the player\'s card)\n\n'
        'Note: Substitutes also affect the Team OVR, so remove them from the reserves first.'
    )
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        total_base_ovr, total_ranks = map(int, message.text.split())

        team_ovr = math.ceil(total_base_ovr / 11) + math.ceil(total_ranks / 11)
        next_upgrade_base_ovr = math.ceil(total_base_ovr / 11) * 11 + 1 - total_base_ovr
        next_upgrade_rank = math.ceil(total_ranks / 11) * 11 + 1 - total_ranks

        response = (
            f"Your Team OVR: {team_ovr}\n"
            f"Next Upgrade (Base OVR): {next_upgrade_base_ovr}\n"
            f"Next Upgrade (Rank): {next_upgrade_rank}"
        )

        bot.send_message(message.chat.id, response)
    except ValueError:
        error_message = (
            'Error: Please enter valid numeric values for Total Base OVR and Total Ranks.\n\n'
            'Instructions:\n'
            'Send your total base OVRs and total ranks in a single message, separated by a space.\n'
            'For example: `985 46`'
        )
        bot.send_message(message.chat.id, error_message)

if __name__ == '__main__':
    bot.polling()
