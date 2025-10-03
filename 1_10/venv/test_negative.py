import requests

base_url = "https://jsonplaceholder.typicode.com"

def test_with_invald_data():
    response = requests.get(f'{base_url}/posts/999')
    assert response.status_code == 404

def test_get_invalid_status():
    resp = requests.post(f"{base_url}/commments")
    assert resp.status_code == 404

def test_put_without_data():
    payload={}
    new_response = requests.put(f'{base_url}/comments/1', json=payload)
    new_data = new_response.json()
    print(new_data)
    assert new_response.status_code==200
    assert type(new_data)==dict

def test_wrong_endpoint():
    resp = requests.get(f"{base_url}/not_exist")
    assert resp.status_code == 404

def test_put_one_data():
    payload={'email': 'some@mail.com'}
    new_response = requests.put(f'{base_url}/comments/1', json=payload)
    assert new_response.status_code==200

def test_put_without_body():
    response = requests.put(f"{base_url}/comments/1")
    assert response.status_code == 200

def test_patch_without_data():
    payload={}
    new_response = requests.patch(f'{base_url}/comments/1', json=payload)
    new_data = new_response.json()
    print(new_data)
    assert new_response.status_code==200
    assert type(new_data)==dict

def test_patch_invalid_id():
    resp = requests.patch(f"{base_url}/comments/999999", json={"email": "wrong@mail.com"})
    assert resp.status_code ==200
    # print(resp.status_code)

def test_with_invalid_queryparams():
    response = requests.get(f"{base_url}/posts?caxik=asd")
    assert response.status_code==200

def test_with_negative_id():
    response = requests.get(f"{base_url}/posts?-66")
    assert response.status_code == 200