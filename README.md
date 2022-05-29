# yaohaoqi

一个用 wxpython 实现的摇号器

依赖:

openpyxl, wxpython

使用:

1. 首先要有一个有“姓名”或“名字”一栏的 Excel 表格，如文件"example.xlsx"所示。
   ![example.xlsx](./example.png)

2. 如果电脑上有 python，请确保已安装以上依赖。如果没有，则在终端输入:

   ```sh
   python3 -m pip install wxpython openpyxl # Windows
   pip3 install wxpython openpyxl # *nix
   ```

3. 运行程序:

   ```sh
   python3 QuantomPhysics.py
   ```

   打开后会出现程序主体:
   ![main](./main.png)
   (窗口可能不完整，往下拉就行)

   这时应当去右上角打开文件:
   ![open_file_mac](./open_file_mac.png)
   (mac)

(目前正在想办法打包成可执行文件)
