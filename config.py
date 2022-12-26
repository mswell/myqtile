# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Programs
terminal = "wezterm"
web_browser = "brave"

# Quick Settings
default_font = "JetBrainsMono Nerd Font"
default_font_size = 18
bar_spacing = 12
bar_padding = 20
part_padding = 22
bar_top_height = 28
bar_bottom_height = 28
window_gap_size = 15

# Presets: , , ██, ░▒▓▓▒░, 
bar_left = ""
bar_right = ""
#
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


# Colors
catppuccin = {
    "Black": "#1a1826",
    "Rosewater": "#f5e0dc",
    "Flamingo": "#f2cdcd",
    "Pink": "#f5c2e7",
    "Mauve": "#cba6f7",
    "Red": "#f38ba8",
    "Maroon": "#eba0ac",
    "Peach": "#fab387",
    "Yellow": "#f9e2af",
    "Green": "#a6e3a1",
    "Teal": "#94e2d5",
    "sky": "#89dceb",
    "Sapphire": "#74c7ec",
    "Blue": "#89b4fa",
    "Lavender": "#b4befe",
    "Text": "#cdd6f4",
    "Subtext1": "#bac2de",
    "Subtext0": "#a6adc8",
    "Overlay2": "#9399b2",
    "Overlay1": "#7f849c",
    "Overlay0": "#6c7086",
    "Surface2": "#585b70",
    "Surface1": "#45475a",
    "Surface0": "#313244",
    "Base": "#1e1e2e",
    "Mantle": "#181825",
    "Crust": "#11111b",
}
mod = "mod4"
# terminal = guess_terminal()


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(
        [mod, "shift"], "D", lazy.spawn("rofi -show drun"), desc="Launch an application"
    ),
    # Polybar Stuff
    Key([mod], "b", lazy.spawn("polybar main"), desc="Spawn Polybar."),
    Key([mod, "shift"], "b", lazy.spawn("pkill polybar"), desc="Kill Polybar."),
    # Picom Stuff
    Key(
        [mod, "control"],
        "p",
        lazy.spawn("picom -b --config ~/.config/picom.conf"),
        desc="Start Picom.",
    ),
    Key([mod, "shift"], "p", lazy.spawn("pkill picom"), desc="Stop Picom."),
    # Poweroff Menu
    Key(
        [mod],
        "p",
        lazy.spawn(os.path.expanduser("~/.config/qtile/power_menu.sh")),
        desc="Launch the power menu.",
    ),
    # Flameshot
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Take a screenshot."),
]

# groups = [Group(i) for i in "123456789"]

groups = [
    Group(
        "1",
        label="",
        matches=[Match(wm_class="brave")],
        layout="max",
    ),
    Group(
        "2",
        label="",
        layout="tile",
    ),
    Group(
        "3",
        label="",
        layout="tile",
    ),
    Group(
        "4",
        label="",
        layout="tile",
    ),
    Group(
        "5",
        label="",
        layout="tile",
    ),
    Group(
        "6",
        label="",
        layout="tile",
    ),
    Group(
        "7",
        label="",
        layout="tile",
    ),
    Group(
        "8",
        label="",
        layout="Tile",
    ),
    Group(
        "9",
        label="",
        matches=[Match(wm_class="discord")],
        layout="max",
    ),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Max(),
    layout.MonadTall(
        margin=window_gap_size,
        border_width=2,
        border_normal=catppuccin["Black"],
        border_focus=catppuccin["Mauve"],
    ),
]

widget_defaults = dict(
    font=default_font,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(),
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    padding=5,
                    fontsize=17,
                    foreground=catppuccin["Crust"],
                    background=catppuccin["Blue"],
                ),
                widget.TextBox(
                    text=bar_right,
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Blue"],
                ),
                widget.GroupBox(
                    highlight_method="text",
                    this_current_screen_border=catppuccin["Green"],
                    urgent_alert_method="text",
                    urgent_text=catppuccin["Red"],
                    background=catppuccin["Base"],
                    active=catppuccin["Text"],
                    inactive=catppuccin["Surface0"],
                    fontsize=15,
                    disable_drag=True,
                ),
                widget.TextBox(
                    text=bar_right,
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Surface0"],
                    foreground=catppuccin["Base"],
                ),
                widget.WindowName(
                    background=catppuccin["Surface0"],
                ),
                widget.TextBox(
                    text=bar_left,
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Surface0"],
                    foreground=catppuccin["Lavender"],
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/Icons")],
                    scale=0.7,
                    background=catppuccin["Lavender"],
                ),
                widget.TextBox(
                    text=bar_left,
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Lavender"],
                    foreground=catppuccin["Sapphire"],
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background=catppuccin["Sapphire"],
                    foreground=catppuccin["Mantle"],
                ),
                widget.TextBox(
                    text=bar_left,
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Sapphire"],
                    foreground=catppuccin["Base"],
                ),
                widget.Systray(
                    background=catppuccin["Base"],
                ),
                widget.TextBox(
                    text=bar_left,
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.Clock(
                    format="%a %Y-%m-%d",
                    background=catppuccin["Green"],
                    foreground=catppuccin["Mantle"],
                ),
                widget.TextBox(
                    text=bar_left,
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Green"],
                    foreground=catppuccin["Mantle"],
                ),
                widget.TextBox(
                    text=" ",
                    background=catppuccin["Mantle"],
                    foreground=catppuccin["Red"],
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            os.path.expanduser("~/.config/qtile/power_menu.sh")
                        ),
                    },
                ),
            ],
            24,
            background=catppuccin["Base"],
            foreground=catppuccin["Text"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
