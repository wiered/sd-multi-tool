class WebUICommandGenerator:
    def __init__(self):
        self._command = ""
        self.args = {
            "auto update": False,
            "cache cleaner": False,
            "pytorch cuda alloc conf": False,
            "xformers(Nvid)": False,
            "opt-sdp(AMD)": False,
            "medvram": False,
            "medvram-sdxl": False,
            "lowvram": False,
            "no half": False,
            "no half vae": False,
            "auto launch": False,
            "dark theme": False,
            "listen": False,
            "safetensors fast gpu": False,
            "cuda visible devices": False,
            "lazy loading": False,
        }
        self.max_threads = 0


    @property
    def command_line_args(self):
        command_line_args = "set COMMANDLINE_ARGS="
        if self.args.get("xformers(Nvid)"):
            command_line_args += " --xformers"
        if self.args.get("opt-sdp(AMD)"):
            command_line_args += " --opt-sdp-attention"
        if self.args.get("medvram"):
            command_line_args += " --medvram"
        if self.args.get("medvram-sdxl"):
            command_line_args += " --medvram-sdxl"
        if self.args.get("lowvram"):
            command_line_args += " --lowvram"
        if self.args.get("no half"):
            command_line_args += " --no-half"
        if self.args.get("no half vae"):
            command_line_args += " --no-half-vae"
        if self.args.get("auto launch"):
            command_line_args += " --autolaunch"
        if self.args.get("dark theme"):
            command_line_args += " --theme=dark"
        if self.args.get("listen"):
            command_line_args += " --listen"
        
        return command_line_args


    @property
    def command(self):
        self._command = "@echo off\n"
        if self.args.get("auto update"):
            self._command += "git pull\n"
        if self.args.get("cache cleaner"):
            self._command += "\n"
            self._command += "for /d %%x in (tmp\\tmp*,tmp\pip*,tmp\gradio\*) do rd /s /q \"%%x\" 2>nul || (\"%%x\" && exit /b 1) & del /q tmp\\tmp* > nul 2>&1 & rd /s /q pip\cache 2>nul\n"
            self._command += "set APPDATA=tmp\n"
            self._command += "set USERPROFILE=tmp\n"
            self._command += "set TEMP=tmp\n"
            self._command += "\n"
        if self.args.get("lazy loading"):
            self._command += "set CUDA_MODULE_LOADING=LAZY\n"
        if self.max_threads > 0:
            self._command += f"set NUMEXPR_MAX_THREADS={self.max_threads}\n"
        if self.args.get("pytorch cuda alloc conf"):
            self._command += "set PYTORCH_CUDA_ALLOC_CONF=garbage_collection_threshold:0.9,max_split_size_mb:512\n"
        if self.args.get("safetensors fast gpu"):
            self._command += "set SAFETENSORS_FAST_GPU=1\n"
        if self.args.get("cuda visible devices"):
            self._command += "set CUDA_VISIBLE_DEVICES=0\n"
        
        self._command += self.command_line_args + "\n"
        self._command += "\ncall webui.bat"
        return self._command
    

    @command.setter
    def command(self, value):
        self._command = value
