def test_unregister_success_and_errors(client):
    activity = "Chess Club"
    # Existing seeded participant
    email = "michael@mergington.edu"

    # Ensure participant exists initially
    before = client.get("/activities").json()
    assert email in before[activity]["participants"]

    # Delete participant
    resp = client.delete(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert "Removed" in resp.json().get("message", "")

    # Verify participant removed
    after = client.get("/activities").json()
    assert email not in after[activity]["participants"]

    # Deleting non-existent participant should return 404
    resp2 = client.delete(f"/activities/{activity}/signup", params={"email": "noone@example.com"})
    assert resp2.status_code == 404

    # Unknown activity returns 404
    resp3 = client.delete("/activities/NoSuchActivity/signup", params={"email": "a@b.c"})
    assert resp3.status_code == 404
