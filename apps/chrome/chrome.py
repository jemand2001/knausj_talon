from talon import ctrl, ui, Module, Context, actions, clip, app

ctx = Context()
mod = Module()

mod.apps.chrome = "app.name: Google Chrome"
mod.apps.chrome = "app.name: Google-Chrome"
mod.apps.chrome = "app.name: chrome.exe"

ctx.matches = r"""
app: chrome
"""


@ctx.action_class("user")
class user_actions:
    def tab_jump(number: int):
        if number < 9:
            if app.platform == "mac":
                actions.key("cmd-{}".format(number))
            else:
                actions.key("ctrl-{}".format(number))

    def tab_final():
        if app.platform == "mac":
            actions.key("cmd-9")
        else:
            actions.key("ctrl-9")

    def new_tab():
        if app.platform == "mac":
            actions.key("cmd-t")
        else:
            actions.key("ctrl-t")

@mod.action_class
class chrome:
    def new_tab():
        """open a new tab"""
