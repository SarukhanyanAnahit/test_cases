import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://demoqa.com"

def random_string(chars, length):
    mstr=""
    for i in range(length):
        mstr+=random.choice(chars)
    return mstr

def test_add_user_and_token():
    payload = {"userName": f"{random_string('abcdefghijklmnopqrstuvwzxyz12345678910', 10)}", "password": "Niki2025-t@a"}
    user = requests.post(f"{BASE_URL}/Account/v1/User", json=payload)
    assert user.status_code ==200 or 201
    data=user.json()
    user_id = data.get("userID")
    print(user_id)
    print(data)

    token_res = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=payload)
    assert token_res.status_code == 200
    token = token_res.json()["token"]
    print(token)

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    books_res = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    assert books_res.status_code == 200
    books = books_res.json()["books"]
    assert len(books) > 0
    first_isbn = books[0]["isbn"]
    assert type(first_isbn)==str

    add_payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": first_isbn}]
    }
    add_res = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=add_payload, headers=headers)
    assert add_res.status_code ==200 or 201

    delete_payload = {"isbn": first_isbn, "userId": user_id}
    delete_res = requests.delete(f"{BASE_URL}/BookStore/v1/Book", json=delete_payload, headers=headers)
    assert delete_res.status_code ==204

def test_book_adding_without_token():
    payload = {"userName": f"{random_string('abcdefghijklmnopqrstuvwzxyz12345678910', 10)}", "password": "Niki2025-t@a"}
    user = requests.post(f"{BASE_URL}/Account/v1/User", json=payload)
    assert user.status_code == 200 or 201
    user_id = user.json().get("userID")
    print(user_id)
    books_res = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    assert books_res.status_code == 200
    books = books_res.json()["books"]
    assert len(books) > 0
    first_isbn = books[0]["isbn"]

    add_payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": first_isbn}]
    }
    add_res = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=add_payload)
    assert add_res.status_code == 401

def test_ui():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/login")
    time.sleep(2)
    login = '084c818nfe'
    password = 'Niki2025-t@a'
    username=driver.find_element(By.ID, 'userName')
    username.send_keys(login)
    passw=driver.find_element(By.ID, 'password')
    passw.send_keys(password)
    log_btn=driver.find_element(By.ID, 'login')
    log_btn.click()
    time.sleep(2)
    assert '/profile' in driver.current_url

    driver.get("https://demoqa.com/books")
    time.sleep(2)
    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("Git Pocket Guide")
    time.sleep(2)
    book_titles = driver.find_element(By.CLASS_NAME, "action-buttons")
    assert 'git' in book_titles.text.lower()

    #CANT ADD TO FAVORITES
    time.sleep(2)
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "/login" in driver.current_url
    driver.quit()
def test_login_invalid():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/login")
    time.sleep(2)
    username = driver.find_element(By.ID, 'userName')
    passw = driver.find_element(By.ID, 'password')
    username.send_keys('sdsdssdf54')
    passw.send_keys('dsdff')
    log_btn = driver.find_element(By.ID, 'login')
    log_btn.click()
    time.sleep(2)
    paragraph=driver.find_element(By.ID, "name")
    assert 'Invalid username or password!'in paragraph.text
    driver.quit()

