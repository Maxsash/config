import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile
from libqtile.widget import Spacer

#Swapped mod1(now default mod) and mod4
#mod4 = super key
mod = "mod1"

mod1 = "mod4"
mod2 = "control"
home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

myTerm = "kitty" # My terminal of choice

keys = [



# ALT + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "d", lazy.spawn('nwggrid -p -o 0.4')), #Grauda settings
    Key([mod], "Escape", lazy.spawn('xkill')), #Click on anything to kill it
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "x", lazy.shutdown()),

# ALT + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn('dolphin')),
    #Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),

# SUPER + ... KEYS

    Key([mod1], "p", lazy.spawn('pamac-manager')),
    Key([mod1], "m", lazy.spawn('pcmanfm')),

# SCREENSHOTS

    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures/screenshots')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod,mod1], "k", lazy.layout.flip_up()),
    Key([mod,mod1], "j", lazy.layout.flip_down()),
    Key([mod,mod1], "l", lazy.layout.flip_right()),
    Key([mod,mod1], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

         ### Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),



# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod1], "Tab", lazy.screen.next_group()),
        Key([mod1, "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

# COLORS FOR THE BAR

def init_colors():
    return [["#010400", "#010400"], # color 0 background
            ["#FFBA08", "#FFBA08"], # color 1 foreground
            ["#E8E9EB", "#E8E9EB"], # color 2 font color
            ["#E4572E", "#E4572E"], # color 3 border-line color primary
            ["#007AB8", "#007AB8"], # color 4 border-line color secondary
            ["#4F76C7", "#4F76C7"], # color 5
            ["#E1ACFF", "#E1ACFF"], # color 6
            ["#ECBBFB", "#ECBBFB"], # color 7
            ["#000000", "#000000"], # color 8
            ["#c40234", "#c40234"], # color 9
            ["#ffd47e", "#ffd47e"]] # color 10

colors = init_colors()


# LAYOUTS

def init_layout_theme():
    return {"margin":4,
            "border_width":2,
            "border_focus": colors[3],
            "border_normal": colors[4]
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=4, border_width=2, border_focus=colors[3][0], border_normal=colors[4][0]),
    layout.MonadWide(margin=16, border_width=2, border_focus=colors[3][0], border_normal=colors[4][0]),
    #layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Floating(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Max(**layout_theme),
    #layout.Columns(**layout_theme),
    layout.Stack(**layout_theme),
    #layout.Tile(**layout_theme),
    layout.TreeTab(
        sections=['FIRST', 'SECOND'],
        bg_color = '#141414',
        active_bg = '#0000ff',
        inactive_bg = '#1e90ff',
        padding_y =5,
        section_top =10,
        panel_width = 280),
    #layout.VerticalTile(**layout_theme),
    #layout.Zoomy(**layout_theme)
]
def base(fg='text', bg='dark'):
    return {'foreground': colors[1],'background': colors[0]}


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 9,
                padding = 2,
                background=colors[0])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

                 widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[0]
                        ),              #
               widget.Image(
                       filename = "~/.config/qtile/icons/garuda-red.png",
                       iconsize = 9,
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('jgmenu_run')}
                       ),
               widget.GroupBox(

            **base(bg=colors[0]),
            font='UbuntuMono Nerd Font',

                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 2,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 3,

            active=colors[3],
            inactive=colors[4],
            rounded= True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors[3],
            this_current_screen_border=colors[3],
            this_screen_border=colors[3],
            other_current_screen_border=colors[4],
            other_screen_border=colors[4],
            disable_drag=True
                        ),

                widget.TaskList(
                    highlight_method = 'border', # or block
                    icon_size=17,
                    max_title_width=150,
                    rounded=True,
                    padding_x=10,
                    padding_y=0,
                    margin_y=0,
                    fontsize=14,
                    border=colors[3],
                    foreground=colors[1],
                    margin=2,
                    txt_floating='🗗',
                    txt_minimized='>_ ',
                    borderwidth = 1,
                    background=colors[0],
                    #unfocused_border = 'border'
                ),

               widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[1],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
               widget.CurrentLayout(
                      font = "Noto Sans Bold",
                      fontsize = 12,
                      foreground = colors[1],
                      background = colors[0]
                        ),

                widget.Net(
                         font="Noto Sans",
                         fontsize=12,
                        # Here enter your network name
                         interface=["wlp3s0"],
                         format = '{down} ↓↑ {up}',
                         foreground=colors[1],
                         background=colors[0],
                         padding = 0,
                         ),
               widget.Clock(
                        foreground = colors[1],
                        background = colors[0],
                        fontsize = 12,
                        format="%d-%m || %H:%M"
                        ),

               widget.Systray(
                       background=colors[0],
                       icon_size=20,
                       padding = 4
                       ),

              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.85, background= "000000")),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.85, background= "000000"))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    #########################################################
    ################ assgin apps to groups ##################
    #########################################################
    d["1"] = ["Alacritty", "Kitty",
                "alacritty", "kitty", ]
    d["2"] = [ "Firefox", "Google-chrome",
                 "firefox", "google-chrome", ]
    d["8"] = [ "TelegramDesktop", "Discord",
                "telegramDesktop", "discord", ]
    d["4"] = ["pcmanfm", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
               "pcmanfm", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
     ##########################################################
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},
    {'wmclass': 'lxpolkit'},
    {'wmclass': 'Lxpolkit'},
    {'wmclass': 'yad'},
    {'wmclass': 'Yad'},


],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
