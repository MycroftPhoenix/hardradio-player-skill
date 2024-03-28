from mycroft import MycroftSkill, intent_file_handler


class HardradioPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('player.hardradio.intent')
    def handle_player_hardradio(self, message):
        self.speak_dialog('player.hardradio')


def create_skill():
    return HardradioPlayer()

