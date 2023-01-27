rt bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook, layout, bar, widget
import os
import subprocess
import re
from libqtile.widget import base, Spacer 
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"
terminal = "alacritty"
browser2 = "brave"
browser1 = "librewolf"
editor_cmd= "alacritty -e vim"
ide = "emacs"
#ide = "vscodium"
file_manager = "thunar"
run_prompt ="dmenu_run"

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
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"), # Toggle between split and unsplit sides of stack.  # Split = all windows displayed # Unsplit = 1 window displayed, like Max layout, but still with # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "q", lazy.spawn("archlinux-logout"), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),  
    Key([mod], "n", lazy.window.toggle_minimize(), desc="Toggle minimize"),  
    # Application launchers
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run"), desc="Run dmenu"),
    Key([mod, "shift"], "e", lazy.spawn(ide), desc="Open ide gui"),
    Key([mod, "shift"], "v", lazy.spawn(editor_cmd), desc="Open vim in a terminal"),
    Key([mod], "o", lazy.spawn("libreoffice"), desc="Open libreoffice"),
    Key([mod, "shift"], "f", lazy.spawn(file_manager), desc="Open thunar"),
    Key([mod], "w", lazy.spawn(browser1), desc="Open brave"),
    Key([mod, "shift"], "w", lazy.spawn(browser2), desc="Open librewolf"),
    Key([mod, "shift"], "m", lazy.spawn("deadbeef"), desc="Open deadbeef"),
    Key([mod, "shift"], "d", lazy.spawn("discord"), desc="Open discord"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch flameshot"),
]

groups = [Group(i) for i in "123456789"]

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
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_width= 3,
        margin = 5,
        border_focus = "#232A2E",
        border_normal = "#262626",
        ),
    layout.Max(
        border_focus = "#232A2E",
        border_normal = "#4F585E",
    ),
     # layout.Stack(num_stacks=2),
  
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_focus = "#232A2E",
        border_normal = "#4F585E",
        margin = 5,
    ),
    layout.MonadWide(
        border_focus = "#232A2E",
        border_normal = "#4F585E",
        margin = 5,
    ),
    layout.RatioTile(
        border_focus = "#232A2E",
        border_normal = "#4F585E",
        margin = 5,
    ),
    layout.Tile(
        border_focus = "#232A2E",
        border_normal = "#4F585E",
        margin = 5,
    ),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = [["#d3c6aa"],
          ["#543a48"],
          ["#514045"],
          ["#425047"],
          ["#3a515d"],
          ["#4d4c43"],
          ["#2d353b"],
          ["#343f44"],
          ["#475258"],
]

defaut_font = "Cantarell"

powerline = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_x=-2, filled=True, size = 8),
        PowerLineDecoration(path="arrow_right", padding_y=0)
    ]
}

powerline_left = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_x=-2, filled=True, size = 8),
        PowerLineDecoration(path="arrow_left", padding_y=0)
    ]
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                background = colors[8],
                length = 6,   
                ),
                widget.CurrentLayout(
                    foreground = colors[0],
                    background = colors[8],
                    **powerline_left,

                ),
                widget.GroupBox(
                    background = colors[7],
                    block_highlight_text_color = colors[0],
                    foreground = colors[0],
                    inactive = colors[0],
                    highlight_method = 'block',
                    **powerline_left,
                ),
                widget.TaskList(
                    icon_size = 20,
                    background = colors[6],
                    **powerline,
                ),
                widget.ThermalSensor(
                    background = colors[5],
                    tag_sensor = 'edge',
                    **powerline,
                ),
                widget.Net(
                    font = defaut_font,
                    background = colors[4],
                    prefix ='M',
                    **powerline,
                ),
                widget.Memory(
                    background = colors[3],
                    measure_mem ='M',
                    **powerline,
                ),
                widget.Systray(
                    padding = 5,
                    background = colors[2],
                    foreground = colors[0],
                    icon_size = 20,
                ),
                #Spacer is to fix issue with the systray
                widget.Spacer(
                    background = colors[2],
                    length = 1,
                    **powerline,
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    padding = 4,
                    background = colors[1],
                ),
            ],
            28,
        background = "#2d353b",
        opacity = 1.0,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = "#232A2E",
    border_normal = "#4F585E",
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

wmname = "qtile"

@hook.subscribe.startup_once
def autostart():
    processes = [
        ['sh', '.config/autostart.sh'],
        ['feh', '--bg-scale', '/home/zhawitche/.config/qtile/wallpapers/forest-fog.jpg'],
        ['swaybg', '-i', '/home/zhawitche/.config/qtile/wallpapers/forest-fog.jpg'],
    ]

    for p in processes:
        subprocess.Popen(p)
