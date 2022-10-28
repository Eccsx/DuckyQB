from duckyqb import story, level, character
import json

if __name__ == "__main__":
    story.begins()
    level.load("test")
    ducky = character.Ducky()

    # # HELP DUCKY HERE #
    # ducky.turn_right()
    # ducky.go_forward()
    # ducky.go_forward()
    # ducky.turn_right()
    # ducky.go_forward()
    # ducky.turn_left()
    # ducky.go_forward()
    # # END #

    story.ends()
