import ctypes
import sys
import zipfile
from threading import Thread

import psutil 
import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from pynvml import *

from windows import (
    Ui_MainWindow, Ui_PromptView, 
    Ui_SDPromptReaderDownloader, StylesEditorDialog
    )
from widgets import ImageScene
from core import WebUICommandGenerator, Downloader

SDMT_BAT_FILENAME = "sdmt_start.bat"

class SDMultiTool(QMainWindow):
    def __init__(self):
        super(SDMultiTool, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.run_webui = WebUICommandGenerator()
        self.icon = QtGui.QIcon()
        self.icon.addFile(':/icons/images/mt-logo.ico')

        self.setWindowIcon(self.icon)

        if os.path.exists(SDMT_BAT_FILENAME):
            with open(SDMT_BAT_FILENAME, 'r') as f:
                self.ui.command_editor.setPlainText(f.read())
        else:
            self.ui.command_editor.setPlainText(self.run_webui.command)

        # setting up buttons
        self.ui.styles_editor_button.clicked.connect(self.start_styles_editor)
        self.ui.prompt_reader_lite_button.clicked.connect(self.start_prompt_reader_lite)
        self.ui.set_recommended_button.clicked.connect(self.set_recommended)
        self.ui.prompt_reader_button.clicked.connect(self.start_prompt_reader)
        self.ui.start_button.clicked.connect(self.start_webui)
        self.ui.about.clicked.connect(
            lambda: os.system("start https://github.com/wiered/sd-multi-tool")
        )

        # setting up command editor 
        # 
        self.ui.command_editor.textChanged.connect(self.command_changed)

        
        # setting up checkboxes
        self.ui.xformers_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.xformers_chbox.text(), 
                self.ui.xformers_chbox.isChecked()
                )
            )
        self.ui.cache_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.cache_chbox.text(), 
                self.ui.cache_chbox.isChecked()
                )
            )
        self.ui.pytorch_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.pytorch_chbox.text(), 
                self.ui.pytorch_chbox.isChecked()
                )
            )
        self.ui.opt_sdp_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.opt_sdp_chbox.text(), 
                self.ui.opt_sdp_chbox.isChecked()
                )
            )

        self.ui.vram_med_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.vram_med_chbox.text(), 
                self.ui.vram_med_chbox.isChecked()
                )
            )
        self.ui.vram_med_sdxl_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.vram_med_sdxl_chbox.text(), 
                self.ui.vram_med_sdxl_chbox.isChecked()
                )
            )
        self.ui.vram_low_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.vram_low_chbox.text(), 
                self.ui.vram_low_chbox.isChecked()
                )
            )

        self.ui.no_half_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.no_half_chbox.text(), 
                self.ui.no_half_chbox.isChecked()
                )
            )
        self.ui.no_half_vae_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.no_half_vae_chbox.text(), 
                self.ui.no_half_vae_chbox.isChecked()
                )
            )
        self.ui.autoupdate_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.autoupdate_chbox.text(), 
                self.ui.autoupdate_chbox.isChecked()
                )
            )
        self.ui.dark_theme_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.dark_theme_chbox.text(), 
                self.ui.dark_theme_chbox.isChecked()
                )
            )
        self.ui.autolaunch_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.autolaunch_chbox.text(), 
                self.ui.autolaunch_chbox.isChecked()
                )
            )
        self.ui.listen_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.listen_chbox.text(), 
                self.ui.listen_chbox.isChecked()
                )
            )
        self.ui.cuda_visible_devices_chox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.cuda_visible_devices_chox.text(), 
                self.ui.cuda_visible_devices_chox.isChecked()
                )
            )
        self.ui.safetensors_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.safetensors_chbox.text(), 
                self.ui.safetensors_chbox.isChecked()
                )
            )
        self.ui.lazy_loading_chbox.stateChanged.connect(
            lambda: self.check_box_state_changed(
                self.ui.lazy_loading_chbox.text(), 
                self.ui.lazy_loading_chbox.isChecked()
                )
            )


    def check_box_state_changed(self, text, state):
        self.run_webui.args.update({text: state})
        self.ui.command_editor.setPlainText(self.run_webui.command)

    
    def set_recommended(self):
        nvmlInit()
        handle = nvmlDeviceGetHandleByIndex(0)
        info: c_nvmlMemory_t = nvmlDeviceGetMemoryInfo(handle)
        gpu_name = nvmlDeviceGetName(handle)
        total_memory = int(info.total/1024**3)

        if "NVIDIA" in gpu_name:
            self.ui.xformers_chbox.setChecked(True)
            if total_memory >= 8:
                self.ui.vram_med_sdxl_chbox.setChecked(True)
            elif total_memory >= 6:
                self.ui.vram_low_chbox.setChecked(True)
            elif total_memory >= 4:
                self.ui.vram_low_chbox.setChecked(True)
                
            self.ui.pytorch_chbox.setChecked(True)
            self.ui.lazy_loading_chbox.setChecked(True)
        
        self.run_webui.max_threads = psutil.cpu_count()
        self.ui.cache_chbox.setChecked(True)
        self.ui.no_half_vae_chbox.setChecked(True)
        self.ui.no_half_chbox.setChecked(True)
        self.ui.safetensors_chbox.setChecked(True)
        self.ui.dark_theme_chbox.setChecked(True)
        

    def command_changed(self):
        ...
    

    def start_webui(self):
        if not os.path.exists(SDMT_BAT_FILENAME):
            f = open(SDMT_BAT_FILENAME, 'w')
            f.close()
        with open(SDMT_BAT_FILENAME, 'w') as f:
            f.write(self.ui.command_editor.toPlainText())
        webui.start()


    def start_styles_editor(self):
        self.style_editor_window = StylesEditorDialog()
        self.style_editor_window.show()
        self.style_editor_window.setWindowIcon(self.icon)

    
    def start_prompt_reader_lite(self):
        self.propmpt_view_window = QDialog()
        self.propmpt_view_window.setWindowIcon(self.icon)
        
        self.propmpt_view = Ui_PromptView()
        self.propmpt_view.setupUi(self.propmpt_view_window)

        self.scene = ImageScene()
        self.scene.set_parent_window(self.propmpt_view)
        self.scene.set_image(":/icons/images/drag_and_drop.png")
        self.propmpt_view.graphicsView.setScene(self.scene)   

        self.propmpt_view_window.show()
        

    def start_prompt_reader(self):
        if os.path.exists("SD Prompt Reader.exe"):
            self.webui = QtCore.QProcess()
            self.webui.start("SD Prompt Reader.exe")
        else:
            self.prompt_reader_downloader_window = QDialog()
            self.prompt_reader_downloader_window.setWindowIcon(self.icon)

            self.propmpt_reader_downloader = Ui_SDPromptReaderDownloader()
            self.propmpt_reader_downloader.setupUi(self.prompt_reader_downloader_window)
            
            self.propmpt_reader_downloader.github_button.clicked.connect(
                lambda: os.system(
                    "start https://github.com/receyuki/stable-diffusion-prompt-reader"
                    )
                )
            self.propmpt_reader_downloader.download_button.clicked.connect(
                lambda: os.system(
                    "start https://github.com/receyuki/stable-diffusion-prompt-reader/releases"
                    )
                )

            self.prompt_reader_downloader_window.show()
            self.prompt_reader_downloader_window.setWindowTitle("SD Prompt Reader Downloader (WIP)")

    
    def init_download(self):
        # I just don't know how to create link to download without it 
        #   expiring in a few hours.
        #   I already tried requesting link from several sources.
        #   But they all have protection and when i try to generate
        #   download link using request post method, they just block me (sad face)
        #   So, if you know what i can do with this, pls, open issue.
        #
        self.propmpt_reader_downloader.label.setText("Downloading file...")
        self.propmpt_reader_downloader.download_button.setEnabled(False)
        self.downloader = Downloader()
        self.downloader.setTotalProgress.connect(
            self.propmpt_reader_downloader.progressBar.setMaximum
            )
        self.downloader.setCurrentProgress.connect(
            self.propmpt_reader_downloader.progressBar.setValue
            )
        self.downloader.succeeded.connect(self.download_succeeded)
        self.downloader.finished.connect(self.download_finished)
        self.downloader.start()


    def download_succeeded(self):
        self.propmpt_reader_downloader.progressBar.setValue(
            self.propmpt_reader_downloader.progressBar.maximum()
            )
        self.propmpt_reader_downloader.label.setText("The file has been downloaded!")


    def download_finished(self):
        with zipfile.ZipFile("tmp.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        
        os.remove("tmp.zip")
        self.prompt_reader_downloader_window.close()
        self.start_prompt_reader()

        del self.downloader


    def closeEvent(self, event):
        if not os.path.exists(SDMT_BAT_FILENAME):
            f = open(SDMT_BAT_FILENAME, 'w')
            f.close()
        with open(SDMT_BAT_FILENAME, 'w') as f:
            f.write(self.ui.command_editor.toPlainText())


def run_webui():
    if not os.path.exists(SDMT_BAT_FILENAME):
        print("Cant run webui in standalone mode")
        return
    os.system(f"call {SDMT_BAT_FILENAME}")


def run_mutitool():
    app = QApplication(sys.argv)
    window = SDMultiTool()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    multi_tool = Thread(target=run_mutitool)
    multi_tool.start()

    webui = Thread(target=run_webui)

    myappid = 'wiered.sdmultitool.sdmultitool.1' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
