# lib/ folder

Place external library files here (such as JDBC driver `.jar` files used by Apache Spark`).
Keeping drivers in the project improves portability and avoids system-level installs.

On macOS and Linux, Spark can use the drivers directly from this folder.

**ADVANCED (Windows on WSL):**
To run Spark on Windows, use WSL:

1. Open **WSL** (Ubuntu) and clone this repo **from inside WSL**, for example:
   `git clone https://github.com/...`
2. In Windows, install the **"WSL – Windows Subsystem for Linux"** extension (`ms-vscode-remote.remote-wsl`) in VS Code.
3. In WSL, navigate into the project folder and run: `code .` This opens the WSL project in VS Code.
4. All notebooks, Spark sessions, and terminal commands will now run **inside WSL**, while the VS Code interface runs normally in Windows.

This setup allows Apache Spark to access the JDBC drivers in the `lib/` folder using Linux paths inside WSL.
