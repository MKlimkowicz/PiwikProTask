import requests
import environment
import pytest

DEFAULT_OFFSET = 0 # default value for offset parameter
DEFAULT_LIMIT = 5 # default value for limit parameter
FIRST_NAME = "" # variable used to collect "name" from the first object in response body
SECOND_NAME = "" # variable used to collect "name" from the second object in response body
FIRST_ID = "" # variable used to collect "id" from the first object in response body
SECOND_ID = "" # variable used to collect "name" from the second object in response body

        

# Test function
def test_get_test_data():
    global FIRST_NAME
    global SECOND_NAME
    global FIRST_ID
    global SECOND_ID
    url = environment.endpoint()
    try:
        response = requests.get(url)
        expected_response = environment.get_expected_correct_response()
        response_data = response.json()

        assert response.status_code == environment.expected_correct_response_code # response code
        assert len(response_data) == DEFAULT_LIMIT
        FIRST_NAME = response_data[0]["name"] # collect "name" from the first object in response body
        FIRST_ID = response_data[0]["id"] # collect "id" from the first object in response body
        SECOND_NAME = response_data[1]["name"] # collect "name" from the second object in response body
        SECOND_ID = response_data[1]["id"] # collect "id" from the second object in response body
        for obj in response_data:
            for key, value in obj.items():
                assert type(value) == expected_response.get(key)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")
# Test function with offset parameter
def test_get_test_data_with_offset(offset=1):
    url = environment.endpoint() + f"?offset={offset}"
    
    try:
        response = requests.get(url)
        expected_response = environment.get_expected_correct_response()
        response_data = response.json()
    
        assert response.status_code == environment.expected_correct_response_code
        assert len(response_data) == DEFAULT_LIMIT
        # asserting second object from request with no offset is now first object given offset=1
        assert SECOND_NAME == response_data[0]["name"] 
        assert SECOND_ID == response_data[0]["id"]
        for obj in response_data:
            for key, value in obj.items():
                assert type(value) == expected_response.get(key)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")

# Test function with limit parameter
def test_get_test_data_with_limit(limit=2):
    url = f"{environment.endpoint()}?limit={limit}"
    
    try:
        response = requests.get(url)
        expected_response = environment.get_expected_correct_response()
        response_data = response.json()
    
        assert response.status_code == environment.expected_correct_response_code
        assert len(response_data) == limit
        for obj in response_data:
            for key, value in obj.items():
                assert type(value) == expected_response.get(key)
    
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")
        

# Test function with search parameter
def test_get_test_data_with_search(search={FIRST_NAME}):
    url = f"{environment.endpoint()}?search={search}"
    
    try:
        response = requests.get(url)
        expected_response = environment.get_expected_correct_response()
        response_data = response.json()
    
        assert response.status_code == environment.expected_correct_response_code
        assert all(FIRST_NAME in obj["name"] for obj in response_data)
        assert all(FIRST_ID in obj["id"] for obj in response_data)
        for obj in response_data:
            for key, value in obj.items():
                assert type(value) == expected_response.get(key)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")
        

# Test function with ID 
def test_get_test_data_with_ID():
    url = f"{environment.endpoint()}{FIRST_ID}"
    
    try:
        response = requests.get(url)
        expected_response = environment.get_expected_correct_response()
        response_data = response.json()
    
        assert response.status_code == environment.expected_correct_response_code
        obj = response_data
        assert FIRST_NAME in obj["name"]
        assert FIRST_ID in obj["id"]
        for key, value in obj.items():
            assert type(value) == expected_response.get(key)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")