import pytest
from flask import json
from app import create_app, db

@pytest.fixture
def app():
    """Create application for the tests."""
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
    return app

@pytest.fixture
def client(app):
    """Test client fixture"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Test CLI runner fixture"""
    return app.test_cli_runner()

@pytest.fixture
def init_database(app):
    """Initialize test database."""
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()
