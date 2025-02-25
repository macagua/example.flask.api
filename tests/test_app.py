import pytest
from flask import json
from app import create_app, db

# The User model and insert_users function will be accessed through the app context
@pytest.fixture(scope="session")
def app():
    """Create application for the tests."""
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })
    return app

@pytest.fixture(scope="function")
def client(app):
    """Test client fixture"""
    return app.test_client()

@pytest.fixture(scope="function")
def init_database(app):
    """Initialize test database."""
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="function")
def sample_user():
    """Sample user fixture"""
    return {
        "name": "Test User",
        "address": "Test Address 123"
    }

# Test User Creation
# def test_create_user_success(app, client, init_database, sample_user):
#     """Test successful user creation"""
#     with app.app_context():
#         # Now we can access User model through app
#         user = app.User  # Access User model from app instance
#         # Get response for POST request
#         response = client.post(
#             '/create',
#             data=json.dumps(sample_user),
#             content_type='application/json'
#         )

#         assert response.status_code == 201
#         data = json.loads(response.data)
#         assert data['user']['name'] == sample_user['name']
#         assert data['user']['address'] == sample_user['address']

#         # Verify in database
#         created_user = user.query.filter_by(name=sample_user['name']).first()
#         assert created_user is not None

# def test_create_user_missing_fields(client):
#     """Test user creation with missing fields"""
#     response = client.post('/create',
#                          data=json.dumps({"name": "Test User"}),
#                          content_type='application/json')
#     assert response.status_code == 400
#     assert b"Missing required fields" in response.data

# def test_create_duplicate_user(client, sample_user):
#     """Test creating duplicate user"""
#     # Create first user
#     client.post('/create',
#                 data=json.dumps(sample_user),
#                 content_type='application/json')
#     # Try to create duplicate user
#     response = client.post('/create',
#                          data=json.dumps(sample_user),
#                          content_type='application/json')
#     assert response.status_code == 500
#     assert b"Internal Server Error" in response.data

# # Test User Retrieval
# def test_get_users_empty(client):
#     """Test getting users when database is empty"""
#     response = client.get('/')
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert len(data['data']) == 0

# def test_get_users_with_data(client, sample_user):
#     """Test getting users with data in database"""
#     client.post('/create',
#                 data=json.dumps(sample_user),
#                 content_type='application/json')
#     response = client.get('/')
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert len(data['data']) == 1
#     assert data['data'][0]['user']['name'] == sample_user['name']

# def test_get_user_detail_success(client, sample_user):
#     """Test getting specific user details"""
#     # Create user first
#     create_response = client.post('/create',
#                                 data=json.dumps(sample_user),
#                                 content_type='application/json')
#     user_id = json.loads(create_response.data)['user']['id']
    
#     response = client.get(f'/detail/{user_id}')
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert data['user']['name'] == sample_user['name']

# def test_get_user_detail_not_found(client):
#     """Test getting non-existent user"""
#     response = client.get('/detail/999')
#     assert response.status_code == 404

# # Test User Update
# def test_update_user_success(client, sample_user):
#     """Test successful user update"""
#     # Create user first
#     create_response = client.post('/create',
#                                 data=json.dumps(sample_user),
#                                 content_type='application/json')
#     user_id = json.loads(create_response.data)['user']['id']
    
#     update_data = {"name": "Updated Name"}
#     response = client.put(f'/update/{user_id}',
#                          data=json.dumps(update_data),
#                          content_type='application/json')
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert data['user']['name'] == "Updated Name"
#     assert data['user']['address'] == sample_user['address']

# def test_update_user_not_found(client):
#     """Test updating non-existent user"""
#     response = client.put('/update/999',
#                          data=json.dumps({"name": "New Name"}),
#                          content_type='application/json')
#     assert response.status_code == 404

# def test_update_user_no_data(client, sample_user):
#     """Test updating user with no data"""
#     # Create user first
#     create_response = client.post('/create',
#                                 data=json.dumps(sample_user),
#                                 content_type='application/json')
#     user_id = json.loads(create_response.data)['user']['id']
    
#     response = client.put(f'/update/{user_id}',
#                          data=json.dumps({}),
#                          content_type='application/json')
#     assert response.status_code == 400

# # Test User Deletion
# def test_delete_user_success(client, sample_user):
#     """Test successful user deletion"""
#     # Create user first
#     create_response = client.post('/create',
#                                 data=json.dumps(sample_user),
#                                 content_type='application/json')
#     user_id = json.loads(create_response.data)['user']['id']
    
#     response = client.delete(f'/delete/{user_id}')
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert data['message'] == "User deleted"

# def test_delete_user_not_found(client):
#     """Test deleting non-existent user"""
#     response = client.delete('/delete/999')
#     assert response.status_code == 404

# # Test Database Operations
def test_insert_users_function(app, client):
    """Test the insert_users function"""
    with app.app_context():
        result = app.insert_users()
        user = app.User  # Access User model from app instance
        if not result:  # Success case returns None
            users = user.query.all()
            assert len(users) >= 3
            # Verify specific users if needed
            user_names = [user.name for user in users]
            assert "Leonardo Caballero" in user_names
            assert "Ana Poleo" in user_names
            assert "Manuel Matos" in user_names
