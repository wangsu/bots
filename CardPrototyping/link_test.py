# test this shit
from CardPrototyping.GenericCard import GenericCardTemplate


class ChangeText(GenericCardTemplate()):
    def on_call(self, arg='hello world'):
        print("PROCESS TEXT RECEIVED: : ", arg)
        arg = arg + " some modification"
        return arg

    def on_method(self):
        return None

    def other_method(self, args):
        return args

# def example():
#     adb_manager_card.on_frame_update_complete(card_test_card.my_fun_bot, 20)
#     card_test_card.on_swipe_complete(adb_manager_card.swipe)
#
#     # some random sleep to decide how long you want the above to run for :D
#     import time
#     time.sleep(run_time)
