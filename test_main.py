import pytest
from io import StringIO
import sys
from main import main


def run_main(input_value):
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: input_value)
        buffer = StringIO()
        m.setattr(sys, "stdout", buffer)
        return_code = main()
        return buffer.getvalue(), return_code


def test_200_success():
    """Test case for valid input """
    output, return_code = run_main("Aditya")
    assert "name --> Aditya" in output
    assert "Your reversed name is aytidA" in output
    assert "Your name has vowels in it." in output
    assert return_code == 200


def test_400_bad_request():
    """Test case for empty input"""
    output, return_code = run_main("")
    assert "Error: Name cannot be empty" in output
    assert return_code == 400


def test_500_server_error():
    """Test case for a server error"""
    with pytest.raises(Exception) as excinfo:
        raise Exception(500,"Server Error")

    assert str(excinfo.value) ==  "(500, 'Server Error')"
