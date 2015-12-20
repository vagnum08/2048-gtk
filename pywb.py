#!/usr/bin/env python
import gtk, webkit
import subprocess
import sys

class browser():

    def __init__(self):
        # Create window
        self.window = gtk.Window()
        self.window.set_icon_from_file('favicon.ico')
        self.window.connect('destroy', self.destroy)
        self.window.set_default_size(800, 800)

        # Create view for webpage
        self.view = gtk.ScrolledWindow()
        self.webview = webkit.WebView()
        self.webview.open('http://localhost:8000/index.html')
        self.webview.connect('title-changed', self.change_title)
        self.webview.connect('load-committed', self.change_url)
        self.view.add(self.webview)

        # Add everything and initialize
        self.container = gtk.VBox()
        self.container.pack_start(self.view)

        self.window.add(self.container)
        self.window.show_all()
        gtk.main()

    def destroy(self,widget):
        subprocess.call(['killall', 'python'])
        gtk.main_quit()
    def load_page(self, widget):
        so_add = self.wow_address_bar.get_text()
        if so_add.startswith('http://') or so_add.startswith('https://'):
            self.webview.open(so_add)
        else:
            so_add = 'http://' + so_add
            self.wow_address_bar.set_text(so_add)
            self.webview.open(so_add)

    def change_title(self, widget, frame, title):
        self.window.set_title('GTK ' + title)

    def change_url(self, widget, frame):
        uri = frame.get_uri()



if __name__ == '__main__':
    web_browser = browser()
