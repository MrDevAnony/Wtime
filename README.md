# Wtime

Wtime is a lightweight and efficient command execution timer designed specifically for Windows.  
It measures the exact runtime duration of any command or program you execute and provides a simple output with the elapsed time.

---

## Features

- Easy to use command-line utility for timing commands on Windows  
- Precise measurement of execution time  
- Lightweight and fast, with no external dependencies  
- Can be integrated into scripts and automation workflows  

---

## Installation

1. Download the latest release binary from the [Releases](https://github.com/MrDevAnony/Wtime/releases) page.  
2. Extract the executable `wtime.exe` to any folder of your choice.  

---

## Usage

Open a Command Prompt or PowerShell window and run:

```bash
wtime <your_command_here>
```

Example:
```bash
wtime ping google.com -n 5
```
This will run the ping command 5 times and display how long it took to execute.

## Adding Wtime to Windows PATH

To run wtime from any location in the command prompt, add its folder to your system PATH environment variable:

1. Press Win + R, type `sysdm.cpl`, and press Enter.

2. In the System Properties window, go to the Advanced tab and click Environment Variables.

3. Under System variables, find and select the Path variable, then click Edit.

4. Click New and add the full path to the folder where you placed wtime.exe. For example:
```bash
C:\Tools\Wtime\
```

5. Click OK on all dialogs to save changes.

6. Restart any open Command Prompt or PowerShell windows to apply the changes.

Now you can simply run:
```bash
wtime <command>
```
from anywhere in your system.

### Example
```bash
wtime curl http://www.gstatic.com/generate_204 -i
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.
