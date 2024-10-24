import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform():
    """tests transform()"""
    result = subprocess.run(
        ["python", "main.py", "transform"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming and loading data..." in result.stdout


def test_query_join():
    """tests query_join()"""
    result = subprocess.run(
        ["python", "main.py", "query_join"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Join Success" in result.stdout


def test_query_aggregate():
    """tests query_aggregate()"""
    result = subprocess.run(
        ["python", "main.py", "query_aggregate"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Aggregate Success" in result.stdout


def test_query_sort():
    """tests query_sort()"""
    result = subprocess.run(
        ["python", "main.py", "query_sort"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Sort Success" in result.stdout


if __name__ == "__main__":
    test_extract()
    test_transform()
    test_query_join()
    test_query_aggregate()
    test_query_sort()
