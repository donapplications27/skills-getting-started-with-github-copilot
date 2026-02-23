def test_signup_success_and_duplicate(client):
    activity = "Chess Club"
    email = "tester1@example.com"

    # Sign up successfully
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")

    # Verify participant present
    all_acts = client.get("/activities").json()
    assert email in all_acts[activity]["participants"]

    # Duplicate signup should return 400
    resp2 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp2.status_code == 400


def test_signup_unknown_activity(client):
    resp = client.post("/activities/NoSuchActivity/signup", params={"email": "a@b.c"})
    assert resp.status_code == 404
