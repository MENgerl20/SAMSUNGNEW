from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
import threading
import time
import random
import platform

# KV Layout string
KV = '''
MDScreen:
    md_bg_color: 0.1, 0.1, 0.1, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "20dp"

        # Header
        MDLabel:
            text: "Samsung A72 Optimizer"
            halign: "center"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 0, 0.8, 1, 1
            size_hint_y: None
            height: self.texture_size[1] + dp(20)

        # Optimization Buttons Area
        MDGridLayout:
            cols: 1
            spacing: "15dp"
            size_hint_y: 0.5
            padding: "10dp"

            MDCard:
                orientation: "horizontal"
                padding: "10dp"
                spacing: "10dp"
                ripple_behavior: True
                on_release: app.run_optimization("RAM")
                md_bg_color: 0.15, 0.15, 0.15, 1
                elevation: 2

                MDIcon:
                    icon: "memory"
                    theme_text_color: "Custom"
                    text_color: 0, 1, 0, 1
                    pos_hint: {"center_y": .5}

                MDLabel:
                    text: "Очистка ОЗУ (RAM Boost)"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    pos_hint: {"center_y": .5}

            MDCard:
                orientation: "horizontal"
                padding: "10dp"
                spacing: "10dp"
                ripple_behavior: True
                on_release: app.run_optimization("CACHE")
                md_bg_color: 0.15, 0.15, 0.15, 1
                elevation: 2

                MDIcon:
                    icon: "trash-can-outline"
                    theme_text_color: "Custom"
                    text_color: 1, 0.5, 0, 1
                    pos_hint: {"center_y": .5}

                MDLabel:
                    text: "Удалить Кэш (Junk Clear)"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    pos_hint: {"center_y": .5}

            MDCard:
                orientation: "horizontal"
                padding: "10dp"
                spacing: "10dp"
                ripple_behavior: True
                on_release: app.run_optimization("BATTERY")
                md_bg_color: 0.15, 0.15, 0.15, 1
                elevation: 2

                MDIcon:
                    icon: "battery-charging-high"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 0, 1
                    pos_hint: {"center_y": .5}

                MDLabel:
                    text: "Экономия Заряда (Battery)"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    pos_hint: {"center_y": .5}

        # Logs Area
        MDLabel:
            text: "System Logs:"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "30dp"

        MDCard:
            size_hint_y: 0.4
            md_bg_color: 0, 0, 0, 1
            padding: "10dp"
            
            MDScrollView:
                id: log_scroll
                
                MDLabel:
                    id: logs_label
                    text: "[color=00ff00]>> Ready to optimize Samsung A72...[/color]"
                    markup: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_text_color: "Custom"
                    text_color: 0.8, 0.8, 0.8, 1
                    font_name: "RobotoMono-Regular" # Use a monospace font if available, or default
                    valign: "bottom"
'''

class OptimizerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def log(self, message, level="INFO"):
        """Adds a message to the log window safely from any thread."""
        color = "ffffff"
        if level == "INFO": color = "00ffff" # Cyan
        if level == "SUCCESS": color = "00ff00" # Green
        if level == "WARN": color = "ffff00" # Yellow
        if level == "ERROR": color = "ff0000" # Red
        
        timestamp = time.strftime("%H:%M:%S")
        formatted_msg = f"\n[{timestamp}] [color={color}]{message}[/color]"
        
        # Schedule UI update on main thread
        Clock.schedule_once(lambda dt: self._update_log_ui(formatted_msg))

    def _update_log_ui(self, message):
        screen = self.root
        logs_label = screen.ids.logs_label
        logs_label.text += message
        # Auto scroll to bottom (rough implementation by resizing label)
        logs_label.height = logs_label.texture_size[1]

    def run_optimization(self, opt_type):
        """Starts the optimization in a separate thread to keep UI smooth."""
        threading.Thread(target=self._optimize_task, args=(opt_type,)).start()

    def _optimize_task(self, opt_type):
        """Simulates optimization logic."""
        
        if opt_type == "RAM":
            self.log(f"Scanning background processes...", "INFO")
            time.sleep(1)
            
            # Simulate killing processes
            apps = ["Instagram", "TikTok", "Chrome", "Facebook Services", "Bixby Agent"]
            for _ in range(3):
                app = random.choice(apps)
                self.log(f"Stopping: {app}", "WARN")
                time.sleep(0.5)
            
            freed = random.randint(150, 450)
            self.log(f"RAM Optimization Complete!", "SUCCESS")
            self.log(f"Freed {freed}MB of Memory.", "SUCCESS")

        elif opt_type == "CACHE":
            self.log("Analyzing storage...", "INFO")
            time.sleep(1.5)
            self.log("Found junk files in /cache/...", "WARN")
            time.sleep(0.5)
            self.log("Clearing application cache...", "INFO")
            time.sleep(1)
            self.log("Removing temporary temp files...", "INFO")
            time.sleep(0.5)
            
            cleared = random.randint(120, 800)
            self.log(f"Cache cleared successfully!", "SUCCESS")
            self.log(f"Reclaimed {cleared}MB of space.", "SUCCESS")

        elif opt_type == "BATTERY":
            self.log("Checking battery health...", "INFO")
            time.sleep(1)
            self.log("Disabling background sync...", "WARN")
            time.sleep(0.5)
            self.log("Adjusting screen brightness...", "INFO")
            time.sleep(0.5)
            self.log("Sleeping unused CPU cores...", "INFO")
            time.sleep(0.8)
            self.log("Battery Saver Mode: ACTIVATED", "SUCCESS")

if __name__ == "__main__":
    OptimizerApp().run()
