import requests

base_url = "https://jsonplaceholder.typicode.com"

def test_get():
    response = requests.get(f'{base_url}/posts/1')
    assert response.status_code==200
    data = response.json()
    print(data)
    assert len(data) > 0
    assert data['userId']==1
    assert 'body' in data
    assert 'quia' in data['body']

def test_comments_with_postId():
    new_response = requests.get(f'{base_url}/comments?postId=1')
    new_data=new_response.json()
    print(new_data)
    assert type(new_data)==list
    assert len(new_data)==5
    assert len(new_data[1]['body'])>=20

def test_using_patch_valid_data():
    payload={
        'id': '5',
        'title': 'somewhere only we knowwww'
    }
    new_response = requests.patch(f'{base_url}/comments/1', json=payload)
    new_data = new_response.json()
    print(new_data)
    assert new_response.status_code==200
    assert type(new_data)==dict
    assert new_data['title']=='somewhere only we knowwww'
    assert 'id' in new_data
    assert 'somewhere' in new_data['title']

def test_using_patch_without_data():
    new_response = requests.patch(f'{base_url}/comments/1', json={})
    new_data = new_response.json()
    assert new_response.status_code==200
    assert isinstance(new_data, dict)


def test_delete_data():
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
    print(response.json())




