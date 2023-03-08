import pytest
import requests
import environment


@pytest.fixture # Request body with type = web, and minimum(0) allowed name characters
def request_body_web():
    return environment.RequestBody(name="", type="web", urls=["http://example.org"])

@pytest.fixture # Request body with type = mobile, max(60) allowed name characters
def request_body_mobile():
    return environment.RequestBody(name="v" * 60, type="mobile", urls=["http://example.org", "http://example.com"])

@pytest.fixture # Request body with type = sharepoint, and max -1(59) allowed name characters
def request_body_sharepoint():
    return environment.RequestBody(name="v" * 59, type="sharepoint", urls=["http://example.com", "http://example.org", "http://example1.com"])



def test_create_data(request_body_web, request_body_mobile, request_body_sharepoint):
    url = environment.endpoint()
    expected_response = environment.get_expected_correct_response()
    # create data with type = web, and minimum allowed name characters
    try:
        response = requests.post(url, json=request_body_web.to_dict())
        # assert response body and code are as expected
        assert response.status_code == environment.expected_correct_response_code # response code
        response_data = response.json()
        obj = response_data
        assert response_data["name"] == request_body_web.name
        assert response_data["type"] == request_body_web.type
        assert set(response_data["urls"]) == set(request_body_web.urls) # Use set() to ignore order of urls
        for key, value in obj.items():
            assert type(value) == expected_response.get(key)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")
    
    # create data with type = mobile, and max allowed name characters
    try:
        response = requests.post(url, json=request_body_mobile.to_dict())
        # assert response body and code are as expected
        assert response.status_code == environment.expected_correct_response_code # response code
        response_data = response.json()
        obj = response_data
        assert response_data["name"] == request_body_mobile.name
        assert response_data["type"] == request_body_mobile.type
        assert set(response_data["urls"]) == set(request_body_mobile.urls) # Use set() to ignore order of urls
        for key, value in obj.items():
            assert type(value) == expected_response.get(key)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")

    
    # create data with type = sharepoint, and max -1 allowed name characters
    try:
        response = requests.post(url, json=request_body_sharepoint.to_dict())
        # assert response body and code are as expected
        assert response.status_code == environment.expected_correct_response_code # response code
        response_data = response.json()
        obj = response_data
        assert response_data["name"] == request_body_sharepoint.name
        assert response_data["type"] == request_body_sharepoint.type
        assert set(response_data["urls"]) == set(request_body_sharepoint.urls) # Use set() to ignore order of urls
        for key, value in obj.items():
            assert type(value) == expected_response.get(key)
    except Exception as e:
        pytest.fail(f"Request failed with exception: {e}")
    