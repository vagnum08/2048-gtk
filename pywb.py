#!/usr/bin/env python
# MIT License
#
# Copyright (c) 2015 vagnum08
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
