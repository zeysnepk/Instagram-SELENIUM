# Instagram Follower Automation Script

This Python script automates the process of logging into an Instagram account, scrolling through the followers list, saving the list of followers to a file and automatically following the followers of another specified account. The script uses the Selenium library to interact with the Instagram web interface.

## Features

- **Login Automation**: Automatically logs into Instagram using credentials stored in a separate file **('loginInfo.py')**.
- **Handle Pop-ups**: Automatically dismisses pop-ups that appear after logging in.
- **Follower Retrieval**: Scrolls through the list of followers of the logged-in account, saving their usernames to a text file.
- **Auto-Follow**: Automatically follows the followers of a specified account.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed.
- **Selenium**: You can install it via pip:
  ```zsh
   pip install selenium
- **ChromeDriver**: : Ensure you have the ChromeDriver that matches your Chrome browser version.
-  A valid Instagram account with login credentials.

## Setup

1. **Clone the Repository**:

      ```zsh
   git clone https://github.com/zeysnepk/Instagram-SELENIUM.git

2. **Run login.py**:

	First run loginInfo.py file to store your Instagram login credential.

      ```zsh
   python loginInfo.py
   
## Usage

1. **Run the Script**:
   
	- The script can be executed from the command line:

	```zsh
   python instagram_automation.py

3. Script Workflow:

   - **Login**: The script logs into Instagram using the credentials provided in the **'loginInfo.py'** file.
   - **Pop-up Handling**: If any pop-ups appear, they are dismissed to ensure smooth execution.
   - **Retrieve Followers**: The script navigates to the logged-in user's profile, opens the followers list, scrolls to the bottom, and saves the followers to a text file **'(followers.txt)'**.
   - **Auto-Follow**: The script navigates to the specified account **'(ACC_NAME)'** and automatically follows all the followers of that account.
  
## Customization

You can customize the script further by modifying the following:

- **Change File Name**: Modify the **'FILE_NAME'** variable in **'twitter_automation.py'** to save usernames for a different file name.
- **Change Account Username**: Modify the **'ACC_NAME'** variable to auto-follow command in a different account.
- **Change XPATH or CSS selectors**: The XPATH or CSS selectors used to find the various elements on the Instagram website.
- **Customize Delay**: You can change the delay time in time.sleep() function.

## Code Explanation

- **login()**: Automates the login process by filling in the username and password fields and clicking the login button.
- **not_today()**: Handles and dismisses any pop-ups that may appear after logging in, such as the "Save Your Login Info?" or "Turn on Notifications" dialogs.
- **get_followers()**: Navigates to the profile of the logged-in user and clicks on the "Followers" button to open the followers list.
- **scroll_to_bottom()**: Scrolls through the followers list until it reaches the bottom. If **'key=True'**, the script will also click the **"Follow"** buttons for each follower in the list.
- **save_to_file()**: Saves the usernames of the followers to a text file. This function extracts the text (usernames) from the followers list and writes them to **'followers.txt'**.
- **auto_follow()**: Automates the process of following all the followers of a specified Instagram account **('ACC_NAME')**. It navigates to the account's followers list and scrolls to the bottom while clicking the **"Follow"** buttons.

## Important Notes

- **Instagram's Rate Limiting**: Instagram has strict rate limiting and anti-bot measures. Use this script responsibly. Rapidly following/unfollowing accounts may result in temporary or permanent bans.
- **Handling Pop-ups**: The script attempts to dismiss pop-ups that may appear. However, Instagram frequently updates its UI, so the XPaths used in the script may need to be updated if the script encounters issues.
- **Error Handling**: Basic error handling is included (e.g., handling pop-up dialogs). However, further enhancements can be made to improve script robustness.
- **WebDriver Compatibility**: Ensure that the version of the WebDriver matches the version of your browser to avoid compatibility issues.

## Disclaimer

This script is intended for educational purposes only. Use it at your own risk. The script author is not responsible for any potential bans or other issues that may arise from using this script on your Instagram account.

## Contribution

Feel free to fork this repository and submit pull requests. Any improvements or new features are welcome!
  
   
