import subprocess

def test_app_runs():
    result = subprocess.run(["py", "app.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Cloud CI Pipeline Running" in result.stdout

if __name__ == "__main__":
    test_app_runs()
    print("Test passed.")