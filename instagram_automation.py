from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import loginInfo

FILE_NAME = "followers.txt" # A text file to save followers' usernames
ACC_NAME = "leake_y34" #Account name whose followers will be followed

jscommand = """
followers = document.querySelector(".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage = followers.scrollHeight;
return lenOfPage;
"""


def login(username, password):
    #Login with the credentials from loginInfo.py
    username_input = browser.find_element(By.NAME, "username")
    username_input.send_keys(username)

    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys(password)

    #Click on the login button
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(10) #Wait for the login process to complete

def not_today():
    #Handle Instagram pop-ups (e.g., "Not Now" or notifications)
    not_now = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div")
    not_now.click()
    time.sleep(2)

    not_notify = browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    not_notify.click()
    time.sleep(2)
    
def get_followers():
    #Navigate to the profile page
    profile_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[8]/div/span/div/a")
    profile_button.click()
    time.sleep(5)
    
    #Click on the followers button to open the followers list
    button_li_list = browser.find_elements(By.CSS_SELECTOR, ".xl565be.x1m39q7l.x1uw6ca5.x2pgyrj")
    followers_button = button_li_list[1]
    followers_button.click()
    time.sleep(5)
        
def scroll_to_bottom(key=False):
    #Scroll down the followers list to the bottom
    scroll = browser.find_element(By.CSS_SELECTOR,".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
    scroll.click() #Focus on the followers list
    scroll = browser.find_element(By.TAG_NAME,"html")
    lenOfPage = browser.execute_script(jscommand) #Execute JavaScript to scroll down
    match = False
    while match == False:
        if key:
            #If key is True, automatically follow users in the list
            box = browser.find_element(By.CSS_SELECTOR, ".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
            box_followers = box.find_element(By.CSS_SELECTOR, "div[style*='height: auto; overflow: hidden auto;']")
            follow_button = box_followers.find_elements(By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30")
            for button in follow_button:
                button.click()
                time.sleep(1) #Wait between each follow action
        lastCount = lenOfPage
        time.sleep(3) 
        scroll.send_keys(u'\uE010') #Scroll down the page using the PageDown key
        lenOfPage = browser.execute_script(jscommand)
        if lenOfPage == lastCount:
                match = True #Exit loop if no new content is loaded
    time.sleep(5) #Wait before exiting the function

def save_to_file(file_name):
    #Save the followers' usernames to a text file
    box = browser.find_element(By.CSS_SELECTOR, ".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
    box_follower = box.find_element(By.CSS_SELECTOR, "div[style*='height: auto; overflow: hidden auto;']")
    followers_list = []
    
    followers = box_follower.find_elements(By.CSS_SELECTOR, "._ap3a._aaco._aacw._aacx._aad7._aade")

    for follower in followers:
        followers_list.append(follower.text) #Collect usernames of followers
        
    #Write the usernames to the specified file
    with open(file_name, "w") as file:
        file.write("Followers:\n") 
        for follower in followers_list:
            file.write(f"{follower}\n")
            
def auto_follow(name):
    #Automatically follow the followers of the specified account
    browser.get(f"https://www.instagram.com/{name}/")
    time.sleep(4)
    
    #Click on the followers button to open the followers list
    button_li_list = browser.find_elements(By.CSS_SELECTOR, ".xl565be.x1m39q7l.x1uw6ca5.x2pgyrj")
    followers_button = button_li_list[1]
    followers_button.click()
    time.sleep(3)
        
    scroll_to_bottom(True) #Scroll through the followers list and follow them automatically
            
if __name__ == "__main__":
    #Main script execution
    browser = webdriver.Chrome()

    # Go to the Instagram website
    browser.get("https://www.instagram.com/")
    time.sleep(3)

    #Login using credentials from loginInfo.py
    username, password = loginInfo.read_info()
    login(username, password)
    
    try:
        not_today() #Handle Instagram pop-ups if they appear
    except:
        pass
    
    get_followers() #Go to the profile page and open the followers list
    scroll_to_bottom() #Scroll through the followers list
    save_to_file(FILE_NAME) #Save the followers' usernames to a file
    
    auto_follow(ACC_NAME) #Automatically follow followers of the specified account

    browser.close() #Close the browser after all actions are completed