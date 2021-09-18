import wx
import os
import data

class Window(wx.Frame):

    def __init__(self, *args, **kw):
        super(Window, self).__init__(*args, **kw)

        self.__data = data.Data()

        self.panel = wx.Panel(self)

        self.nameST = wx.StaticText(self.panel, label="遇事不决，量子力学")
        self.nameST.SetFont(wx.Font(wx.FontInfo(22).Bold()))

        bitmap = wx.Bitmap()
        bitmap.LoadFile("./ButtonPic.jpg")
        self.button = wx.BitmapButton(self.panel, wx.ID_ANY, bitmap)
        self.button.Bind(wx.EVT_BUTTON, self.OnClick)

        self.remindButtonST = wx.StaticText(self.panel, label = "戳上面的图片↑")

        self.modeChooser = wx.RadioBox(self.panel, id=wx.ID_ANY, label="选择模式", choices=["重复模式", "无重复模式"])

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.nameST, wx.SizerFlags().Align(wx.ALIGN_CENTER).Border(wx.ALL, 10))
        sizer.Add(self.button, wx.SizerFlags().Align(wx.ALIGN_CENTER).Border(wx.ALL, 10))
        sizer.Add(self.remindButtonST, wx.SizerFlags().Align(wx.ALIGN_CENTER).Border(wx.ALL, 10))
        sizer.Add(self.modeChooser, wx.SizerFlags().Align(wx.ALIGN_CENTER).Border(wx.ALL, 10))
        self.panel.SetSizer(sizer)

        self.makeMenuBar()

        self.Centre()
    
    
    def makeMenuBar(self):
        fileMenu = wx.Menu()
        openFileItem = fileMenu.Append(-1, "&打开文件...", "打开学生名单")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menubar = wx.MenuBar()
        menubar.Append(fileMenu, "&File")
        menubar.Append(helpMenu, "&Help")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnOpenFile, openFileItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)

    def OnOpenFile(self, event):
        dlg = wx.FileDialog(self, "Choose a file to open", "", "", "*.*")
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            fileDir = os.path.join(self.dirname, self.filename)
            self.__data.openFile(fileDir)
        dlg.Destroy()


    def OnAbout(self, event):
        wx.MessageBox("Copyright@asterich, 2020~114514",
                      "About",
                      wx.OK|wx.ICON_INFORMATION)

    def OnClick(self, event):
        if self.__data.openFileFlg == True:
            mode = self.modeChooser.GetSelection()
            if mode == 0:
                nameStr = self.__data.getRandName_Normal()
            else:
                nameStr = self.__data.getRandName_NoRepetition()
            self.nameST.SetLabel(nameStr)
        else:
            wx.MessageBox("尚未打开文件")


    def OnExit(self, event):
        self.Close(True)

if __name__ == "__main__":
    app = wx.App()
    window = Window(None, title="量子力学摇号器")
    window.Show()
    app.MainLoop()
