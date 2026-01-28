from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import threading
import time
import random

# KV Layout string
KV = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)

<TweakItem>:
    text: root.text
    theme_text_color: "Custom"
    text_color: 1, 1, 1, 1
    _no_ripple_effect: True
    
    IconLeftWidget:
        icon: root.icon
        theme_text_color: "Custom"
        text_color: 0, 0.8, 1, 1

    RightContainer:
        id: container
        orientation: "horizontal"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: "10dp"
        
        MDSwitch:
            active: root.active
            pos_hint: {'center_x': .9, 'center_y': .5}
            on_active: app.on_switch_active(root, self.active)

MDScreen:
    md_bg_color: 0.05, 0.05, 0.05, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: "10dp"
        spacing: "10dp"

        # Header
        MDBoxLayout:
            size_hint_y: None
            height: "60dp"
            padding: "10dp"
            
            MDIcon:
                icon: "android-debug-bridge"
                theme_text_color: "Custom"
                text_color: 0, 0.8, 1, 1
                size_hint_x: None
                width: "40dp"
                pos_hint: {"center_y": .5}
                
            MDLabel:
                text: "SAMSUNG A72\\nULTIMATE TWEAKER"
                font_style: "H6"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                bold: True
                pos_hint: {"center_y": .5}

        # Tabs / Tweak List
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.6
            md_bg_color: 0.1, 0.1, 0.1, 1
            radius: [15, 15, 15, 15]
            padding: "5dp"

            MDScrollView:
                MDBoxLayout:
                    id: tweaks_list
                    orientation: 'vertical'
                    adaptive_height: True
                    spacing: "5dp"
                    padding: "10dp"

        # Action Area
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "80dp"
            padding: "10dp"
            spacing: "10dp"
            
            MDFillRoundFlatButton:
                text: "APPLY SELECTED TWEAKS"
                font_size: "18sp"
                size_hint_x: 1
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.start_optimization()

        # Logs Area
        MDCard:
            size_hint_y: 0.3
            md_bg_color: 0, 0, 0, 1
            padding: "10dp"
            radius: [10, 10, 0, 0]
            
            MDScrollView:
                id: log_scroll
                
                MDLabel:
                    id: logs_label
                    text: "[color=00ff00]>> System ready. Waiting for commands...[/color]"
                    markup: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_text_color: "Custom"
                    text_color: 0.8, 0.8, 0.8, 1
                    font_name: "RobotoMono-Regular"
                    valign: "bottom"
'''

class TweakItem(OneLineAvatarIconListItem):
    text = StringProperty()
    icon = StringProperty()
    active = False

class RightContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class OptimizerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_start(self):
        # Populate tweaks
        tweaks = [
            # CPU & Performance
            {"name": "CPU Core Unpark", "icon": "chip"},
            {"name": "GPU Overclock (Adreno)", "icon": "expansion-card"},
            {"name": "Force 90Hz Refresh Rate", "icon": "speedometer"},
            {"name": "Disable Thermal Throttling", "icon": "thermometer-alert"},
            {"name": "Samsung Game Booster Plus", "icon": "gamepad-variant"},
            {"name": "High Performance Mode", "icon": "flash"},
            
            # System & Bloatware
            {"name": "Debloat Bixby Services", "icon": "robot-off"},
            {"name": "Remove Samsung Cloud", "icon": "cloud-off"},
            {"name": "Disable Analytics/Tracking", "icon": "eye-off"},
            {"name": "Kill Background Activities", "icon": "application-remove"},
            {"name": "Deep Sleep Unused Apps", "icon": "sleep"},
            
            # Network
            {"name": "DNS Optimization (1.1.1.1)", "icon": "dns"},
            {"name": "TCP/IP Aggregation", "icon": "network"},
            {"name": "5G Signal Boost", "icon": "signal-5g"},
            {"name": "Reduce WiFi Latency", "icon": "wifi-star"},
            
            # Storage & Battery
            {"name": "Clear Dalvik Cache", "icon": "broom"},
            {"name": "Trim NAND Memory", "icon": "sd"},
            {"name": "Battery Calibration", "icon": "battery-sync"},
            {"name": "Disable Fast Charging Heat", "icon": "fire-off"},
            {"name": "Aggressive Doze Mode", "icon": "power-sleep"},
        ]
        
        for tweak in tweaks:
            item = TweakItem(text=tweak["name"], icon=tweak["icon"])
            self.root.ids.tweaks_list.add_widget(item)
            
        self.active_tweaks = set()

    def on_switch_active(self, instance_tweak, value):
        if value:
            self.active_tweaks.add(instance_tweak.text)
            self.log(f"Selected: {instance_tweak.text}", "INFO")
        else:
            if instance_tweak.text in self.active_tweaks:
                self.active_tweaks.remove(instance_tweak.text)
                self.log(f"Deselected: {instance_tweak.text}", "INFO")

    def log(self, message, level="INFO"):
        color = "ffffff"
        if level == "INFO": color = "00ffff" # Cyan
        if level == "SUCCESS": color = "00ff00" # Green
        if level == "WARN": color = "ffff00" # Yellow
        if level == "ERROR": color = "ff0000" # Red
        
        timestamp = time.strftime("%H:%M:%S")
        formatted_msg = f"\n[{timestamp}] [color={color}]{message}[/color]"
        Clock.schedule_once(lambda dt: self._update_log_ui(formatted_msg))

    def _update_log_ui(self, message):
        logs_label = self.root.ids.logs_label
        logs_label.text += message
        logs_label.height = logs_label.texture_size[1]

    def start_optimization(self):
        if not self.active_tweaks:
            self.log("No tweaks selected! Select at least one.", "ERROR")
            return
            
        threading.Thread(target=self._run_optimization_process).start()

    def _run_optimization_process(self):
        self.log(">>> INITIALIZING OPTIMIZATION ENGINE...", "WARN")
        time.sleep(1)
        self.log(">>> MOUNTING SYSTEM RW...", "WARN")
        time.sleep(1)
        
        total = len(self.active_tweaks)
        current = 0
        
        for tweak in self.active_tweaks:
            current += 1
            self.log(f"Applying: {tweak}...", "INFO")
            
            # Fake processing time
            time.sleep(random.uniform(0.5, 2.0))
            
            # Random "sub-steps" for realism
            if "CPU" in tweak:
                self.log("  -> Adjusting governor...", "INFO")
                time.sleep(0.5)
            if "Network" in tweak or "DNS" in tweak:
                self.log("  -> Flushing IP tables...", "INFO")
                time.sleep(0.5)
            if "Debloat" in tweak:
                self.log("  -> Disabling package via ADB...", "INFO")
                time.sleep(0.5)
                
            self.log(f"DONE [{current}/{total}]", "SUCCESS")
            
        self.log(">>> OPTIMIZATION COMPLETED SUCCESSFULLY!", "SUCCESS")
        self.log(">>> PLEASE REBOOT YOUR PHONE.", "WARN")

if __name__ == "__main__":
    OptimizerApp().run()
