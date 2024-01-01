from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class TeamOVRCalculatorApp(App):
    def build(self):
        self.title = 'Team OVR Calculator'

        # Widgets
        self.instructions_label = Label(
            text=(
                'Welcome to the Team OVR Calculator!\n\n'
                'Instructions:\n'
                '1. Send your total base OVRs and total ranks in a single message, separated by a space.\n'
                '   For example: `985 46`\n\n'
                '2. The app will calculate your Team OVR and provide next upgrade information.\n\n'
                'Terms Explanation:\n'
                ' - Team OVR: Average Base OVR (rounded up) + Average Rank (rounded up)\n'
                ' - Base OVR: Player\'s base OVR, excluding Training/Rank (if any)\n'
                ' - Rank: Number of ranks in the team (deduct the base OVR of the player\'s card)\n\n'
                'Note: Substitutes also affect the Team OVR, so remove them from the reserves first.'
            ),
            halign='left',
            valign='top',
            padding=(10, 10)
        )
        self.input_text = TextInput(multiline=False)
        self.calculate_button = Button(text='Calculate', on_press=self.calculate)
        self.help_button = Button(text='Help', on_press=self.show_help)

        # Layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.instructions_label)
        layout.add_widget(self.input_text)
        layout.add_widget(self.calculate_button)
        layout.add_widget(self.help_button)

        return layout

    def calculate(self, instance):
        try:
            input_values = self.input_text.text.split()
            total_base_ovr, total_ranks = map(int, input_values)

            team_ovr = math.ceil(total_base_ovr / 11) + math.ceil(total_ranks / 11)
            next_upgrade_base_ovr = math.ceil(total_base_ovr / 11) * 11 + 1 - total_base_ovr
            next_upgrade_rank = math.ceil(total_ranks / 11) * 11 + 1 - total_ranks

            result_text = (
                f"Your Team OVR: {team_ovr}\n"
                f"Next Upgrade (Base OVR): {next_upgrade_base_ovr}\n"
                f"Next Upgrade (Rank): {next_upgrade_rank}"
            )

            self.instructions_label.text = result_text
        except ValueError:
            self.instructions_label.text = 'Error: Please enter valid numeric values.'

    def show_help(self, instance):
        self.instructions_label.text = (
            'Welcome to the Team OVR Calculator!\n\n'
            'Instructions:\n'
            '1. Send your total base OVRs and total ranks in a single message, separated by a space.\n'
            '   For example: `985 46`\n\n'
            '2. The app will calculate your Team OVR and provide next upgrade information.\n\n'
            'Terms Explanation:\n'
            ' - Team OVR: Average Base OVR (rounded up) + Average Rank (rounded up)\n'
            ' - Base OVR: Player\'s base OVR, excluding Training/Rank (if any)\n'
            ' - Rank: Number of ranks in the team (deduct the base OVR of the player\'s card)\n\n'
            'Note: Substitutes also affect the Team OVR, so remove them from the reserves first.'
        )

if __name__ == '__main__':
    TeamOVRCalculatorApp().run()
