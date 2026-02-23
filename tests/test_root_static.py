def test_root_redirect_and_static(client):
    # Don't follow redirects so we can assert the location header
    resp = client.get("/", allow_redirects=False)
    assert resp.status_code in (302, 307)
    assert resp.headers.get("location") == "/static/index.html"

    # Static index should be served
    static = client.get("/static/index.html")
    assert static.status_code == 200
    assert "Mergington High School" in static.text
