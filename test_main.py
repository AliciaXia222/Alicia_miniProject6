"""
Test goes here

"""
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


# def test_transform_load():
#     """tests transfrom_load"""
#     result = subprocess.run(
#         ["python", "main.py", "transform_load"],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0
#     assert "Transforming data..." in result.stdout


# def test_update_record():
#     """tests update_record"""
#     result = subprocess.run(
#         [
#             "python",
#             "main.py",
#             "update_record",
#             "30",
#             "20",
#             "8",
#             "Rain",
#             "2006-1-30",
#             "57",
#         ],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0


# def test_delete_record():
#     """tests delete_record"""
#     result = subprocess.run(
#         ["python", "main.py", "delete_record", "37"],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0


# def test_create_record():
#     """tests create_record"""
#     result = subprocess.run(
#         [
#             "python",
#             "main.py",
#             "update_record",
#             "37",
#             "20",
#             "8",
#             "Rain",
#             "2006-1-30",
#         ],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0


# def test_general_query():
#     """tests general_query"""
#     result = subprocess.run(
#         [
#             "python",
#             "main.py",
#             "general_query",
#             "SELECT * FROM Centralpark WHERE Max_TemperatureF = '37'",
#         ],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0


# def test_read_data():
#     """tests read_data"""
#     result = subprocess.run(
#         ["python", "main.py", "read_data"],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    # test_transform_load()
    # test_create_record()
    # test_read_data()
    # test_update_record()
    # test_delete_record()
    # test_general_query()
