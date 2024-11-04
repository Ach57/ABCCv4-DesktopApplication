# ABCCv4-DesktopApplication
## Overview
ABCCV4.py is the main file of the ABCCV4 desktop application. This application automates manual tasks such as updating data in Google Spreadsheets and generating charts and graphs. It utilizes various libraries to accomplish these tasks.

## Dependencies
## 🛠️ Libraries and Modules Used
- **[gspread](https://github.com/burnash/gspread)**: Python API for Google Sheets
- **[tkinter](https://docs.python.org/3/library/tkinter.html)**: GUI toolkit for Python
- **[PIL (Python Imaging Library)](https://pillow.readthedocs.io/en/stable/)**: Image processing library for Python (use `Pillow` as the updated version)
- **[matplotlib](https://matplotlib.org/)**: Plotting library for generating charts and graphs
- **[datetime](https://docs.python.org/3/library/datetime.html)**: Module for manipulating dates and times
- **[tkinter.filedialog](https://docs.python.org/3/library/tkinter.filedialog.html)**: Module for opening file dialogs in Tkinter applications
- **[tkinter.messagebox](https://docs.python.org/3/library/tkinter.messagebox.html)**: Module for displaying message boxes in Tkinter applications
- **[logging](https://docs.python.org/3/library/logging.html)**: Module for logging messages in the application

## 🔑 Setup Instructions

To run this application, you’ll need a `credentials.json` file. Follow these steps to obtain it:

1. **Create a Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Set up a new project (or select an existing one).

2. **Enable the Google Sheets API**:
   - In the **APIs & Services** section, search for "Google Sheets API" and enable it for your project.
   - Repeat for the "Google Drive API" if you need file access permissions.

3. **Create a Service Account**:
   - In the Cloud Console, go to **APIs & Services > Credentials**.
   - Click **Create Credentials** and select **Service Account**.
   - Complete the service account setup.

4. **Generate the `credentials.json` file**:
   - Under your new service account, click **Add Key** > **Create New Key**.
   - Choose the **JSON** format; this file will download automatically.
   - Rename the file to `credentials.json` and place it in your project’s root directory.

5. **Authorize the Service Account**:
   - Share your Google Sheets document with the service account's email (found in the `credentials.json` file under `client_email`).

Your application will now be able to access Google Sheets using this file. Make sure to keep `credentials.json` secure and **do not share it publicly**.

## Sample:

![Sample](https://github.com/user-attachments/assets/eab4f9f0-5067-4d1b-bee5-5c3502cdd54f)


