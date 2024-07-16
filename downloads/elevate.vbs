
        Set UAC = CreateObject("Shell.Application")
        UAC.ShellExecute "downloads\BraveBrowserSetup32.exe", "", "", "runas", 1
        