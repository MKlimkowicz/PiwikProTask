import pytest
import requests
import environment


# incorrect offset value, string and boolean
@pytest.fixture(params=["incorrect", True])
def offset_value(request):
    return request.param

# incorrect limit value, string and boolean
@pytest.fixture(params=["incorrect", True])
def limit_value(request):
    return request.param

# incorrect search value, integer and boolean
@pytest.fixture(params=[25, True])
def search_value(request):
    return request.param


# Test function with incorrect offset data type
def test_get_incorrect_offset(offset=offset_value):
    url = environment.endpoint() + f"?offset={offset}"
    try:
        response = requests.get(url)
        assert response.status_code == environment.expected_error_response_code # response code
        response_data = response.json()
        assert isinstance(response_data["detail"], list)
        assert isinstance(response_data["detail"][0]["loc"], list)
        assert isinstance(response_data["detail"][0]["msg"], str)
        assert isinstance(response_data["detail"][0]["type"], str)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")

# Test function with incorrect limit data type
def test_get_incorrect_limit(limit=limit_value):
    url = environment.endpoint() + f"?limit={limit}"
    try:
        response = requests.get(url)
        assert response.status_code == environment.expected_error_response_code # response code
        response_data = response.json()
        assert isinstance(response_data["detail"], list)
        assert isinstance(response_data["detail"][0]["loc"], list)
        assert isinstance(response_data["detail"][0]["msg"], str)
        assert isinstance(response_data["detail"][0]["type"], str)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")

# Test function with incorrect search data type
def test_get_incorrect_search(search=search_value):
    url = environment.endpoint() + f"?search={search}"
    try:
        response = requests.get(url)
        assert response.status_code == environment.expected_error_response_code # response code
        response_data = response.json()
        assert isinstance(response_data["detail"], list)
        assert isinstance(response_data["detail"][0]["loc"], list)
        assert isinstance(response_data["detail"][0]["msg"], str)
        assert isinstance(response_data["detail"][0]["type"], str)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")
