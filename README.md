# Zip Combine

Zip 檔案合併

本專案開發主要基於 Python 3.11.5、 PySide6

## 注意事項

**任何檔案在進入此程式使用前，請務必做好備份，並且使用副本來操作。本程式會對匯入的檔案進行讀寫的操作，請在確認新命名的預覽之後再重新命名。**

## 安裝

### 執行檔

支援 Windows_x64 及 Linux_x64 ，請至 [Release](https://github.com/scbmark/zip_combine/releases) 下載。

編譯環境：於 Ubuntu 22.04 x64 的系統環境下，在 Poetry 建立的虛擬環境中用 Nuitka 編譯，C++ 編譯器為 gcc。

### 從原始碼執行

#### 安裝依賴套件

本專案使用 Python 開發，並且用 Poetry 管理依賴套件。下載原始碼之後，至專案根目錄使用 Poetry 建立虛擬環境並安裝依賴套件。

```bash
poetry install  # 建立虛擬環境並安裝依賴套件
```

#### 執行主程式

以上都設定好之後，入口程式為 ```run.py```。進入虛擬環境後，直接執行即可。

```bash
python ./run.py
```

### 從原始碼編譯

如上「[從原始碼執行](#從原始碼執行)」所述，安裝完虛擬環境及設定好模版文件後，使用 Nuitka 進行原始碼打包。

#### Linux

```bash
# Linux
## 安裝依賴
sudo apt install patchelf   # Ubuntu
sudo pacman -S patchelf # Arch Linux

## 開始編譯
python -m nuitka --standalone --static-libpython=no --enable-plugin=pyside6 --follow-imports --include-package=certifi --disable-console --output-dir=output run.py

```

#### Windows

```bash
# Windows
python -m nuitka --standalone --static-libpython=no --enable-plugin=pyside6 --follow-imports --include-package=certifi --disable-console --windows-icon-from-ico=.\statics\icon.ico --output-dir=output run.py
```

執行 output/run.dist 內的執行檔即可。


## 貢獻

感謝您的使用，對於本專案有任何建議或 Bug 的回報，歡迎發 Issue 或者使用 Email 和作者連繫。

## 作者

Mark Hsiao

Email：[Twilight3847@skiff.com](#作者)

## 授權

[GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/)