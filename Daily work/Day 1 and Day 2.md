# Installed Chocolety Python and Manim
- Open Command Prompt or PowerShell as an administrator.
- Install Chocolatey, if not already installed, by running:
  ```powershell
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
  ```
- Install Python using Chocolatey by running:
  ```powershell
  choco install python
  ```
- Verify the Python installation by running:
  ```powershell
  python --version
  ```
- Install Manim using Chocolatey by running:
  ```powershell
  choco install manim
  ```
- Verify the Manim installation by running:
  ```powershell
  manim --version
  ```