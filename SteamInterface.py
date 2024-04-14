import webbrowser


def launch_game(app_id, mod_id):
    url = f"steam://run/{app_id}//{mod_id}"

    webbrowser.open(url)


mod_name = input("Press Enter to continue")

# Mindustry
test_app_id = 1127400

# EAW
definitive_app_id = 32470


launch_game(test_app_id, "")
