from app import create_app


def test_home_page():
    app = create_app({"TESTING": True, "SECRET_KEY": "test-only", "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Stellafy" in response.data
