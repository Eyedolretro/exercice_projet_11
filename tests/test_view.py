import pytest
from calculate.view import display_result, get_input

def test_display_result(capsys):
    # Vérifie le nombre d'arguments requis et adapte ici
    # Si display_result prend uniquement 'result'
    try:
        display_result(result=5)
    except TypeError:
        # Si display_result prend un autre argument obligatoire 'operation', on fournit un dummy
        display_result(result=5, operation="dummy")
    
    captured = capsys.readouterr()
    assert "5" in captured.out

def test_get_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2 + 3")
    result = get_input()
    assert result == "2 + 3"
